from fastapi import APIRouter, Request
from backend.services.recommender import recommend_materials

router = APIRouter()

@router.post("/recommend")
async def recommend(request: Request):
    filters = await request.json()
    results = recommend_materials(filters)
    return results
