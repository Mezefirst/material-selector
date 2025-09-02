import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from services.recommender import recommend_materials, suggest_alternatives, simulate_tradeoff
from services.nlp import parse_user_query
from services.external_sources import fetch_matweb_materials, fetch_material_project_materials

# Initialize database (with fallback handling)
try:
    from backend.database import engine, Base
    from backend.router.material import router as material_router
    Base.metadata.create_all(bind=engine)
    DATABASE_AVAILABLE = True
except Exception as e:
    print(f"Database setup failed: {e}. Running in data-only mode.")
    DATABASE_AVAILABLE = False

# Create FastAPI app
app = FastAPI(title="Material Selector API", version="1.0.0")

# Include database routes if available
if DATABASE_AVAILABLE:
    app.include_router(material_router, prefix="/api")

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

# Pydantic models
class Material(BaseModel):
    name: str
    strength: float
    cost: float
    sustainability: float

class RecommendationRequest(BaseModel):
    min_strength: Optional[float] = None
    max_cost: Optional[float] = None
    min_sustainability: Optional[float] = None
    max_strength: Optional[float] = None
    min_cost: Optional[float] = None
    max_sustainability: Optional[float] = None
    query: Optional[str] = None
    search: Optional[str] = None

# API Routes
@app.get("/")
def read_root():
    return {"message": "Material Selector API is running", "version": "1.0.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "database": DATABASE_AVAILABLE}

@app.post("/recommend", response_model=List[Material])
def recommend(req: RecommendationRequest):
    """Get material recommendations based on filters or natural language query"""
    if req.query:
        filters = parse_user_query(req.query)
        # Merge with explicit filters
        explicit_filters = req.model_dump(exclude_none=True, exclude={"query"})
        filters.update(explicit_filters)
    else:
        filters = req.model_dump(exclude_none=True)
    
    results = recommend_materials(filters)
    return results

@app.post("/alternatives", response_model=List[Material])
def alternatives(material: Material):
    """Get alternative materials similar to the provided material"""
    return suggest_alternatives(material.model_dump())

@app.post("/tradeoff")
def tradeoff(material_a: Material, material_b: Material):
    """Simulate trade-offs between two materials"""
    return simulate_tradeoff(material_a.model_dump(), material_b.model_dump())

@app.get("/external-materials")
def get_external_materials(source: str, query: str):
    """Get materials from external data sources"""
    if source == "matweb":
        return fetch_matweb_materials(query)
    elif source == "materials_project":
        return fetch_material_project_materials(query)
    return {"error": "Unknown source"}

@app.get("/plan_rl")
def plan_rl():
    """Placeholder for RL-driven recommendations"""
    return {"detail": "RL stub: Will optimize recommendations over time based on feedback."}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
