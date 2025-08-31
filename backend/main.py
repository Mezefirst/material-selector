import os
from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List, Optional
from services.recommender import recommend_materials, suggest_alternatives, simulate_tradeoff
from services.nlp import parse_user_query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Material Selector API", version="1.0.0")

# Environment-based CORS configuration
ENV = os.getenv("ENV", "development")
if ENV == "production":
    # In production, specify allowed origins
    allowed_origins = [
        "https://your-frontend-domain.vercel.app",
        "https://your-frontend-domain.netlify.app"
    ]
else:
    # In development, allow all origins
    allowed_origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Material(BaseModel):
    name: str
    strength: float
    cost: float
    sustainability: float

class RecommendationRequest(BaseModel):
    min_strength: Optional[float] = None
    max_cost: Optional[float] = None
    min_sustainability: Optional[float] = None
    query: Optional[str] = None

@app.get("/")
def read_root():
    return {"message": "Material Selector API is running", "version": "1.0.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/recommend", response_model=List[Material])
def recommend(req: RecommendationRequest):
    if req.query:
        filters = parse_user_query(req.query)
    else:
        filters = req.dict(exclude_none=True)
    return recommend_materials(filters)

@app.post("/alternatives", response_model=List[Material])
def alternatives(material: Material):
    return suggest_alternatives(material.dict())

@app.post("/tradeoff")
def tradeoff(material_a: Material, material_b: Material):
    return simulate_tradeoff(material_a.dict(), material_b.dict())

@app.get("/plan_rl")
def plan_rl():
    return {"detail": "RL stub: Will optimize recommendations over time based on feedback."}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
