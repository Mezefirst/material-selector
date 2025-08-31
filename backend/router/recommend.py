from fastapi import APIRouter, Request
from backend.services.recommender import recommend_materials

router = APIRouter()

@router.post("/recommend")
async def recommend(request: Request):
    payload = await request.json()
    filters = payload.get("filters", {})
    query = payload.get("search", "")
    model_type = payload.get("model_type", "xgb")
    results = recommend_materials(filters, query=query, model_type=model_type)
    return results
