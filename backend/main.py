from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List, Optional
from services.recommender import recommend_materials, suggest_alternatives, simulate_tradeoff
from services.nlp import parse_user_query

app = FastAPI()

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
