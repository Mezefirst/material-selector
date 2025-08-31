from fastapi import APIRouter, Request

feedback_router = APIRouter()

@feedback_router.post("/feedback")
async def submit_feedback(request: Request):
    payload = await request.json()
    # Store feedback in database or file
    # Example: {"user_id": ..., "material_id": ..., "liked": True}
    # Use this data to retrain/reweight models periodically
    return {"status": "ok"}
