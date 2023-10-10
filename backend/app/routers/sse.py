from fastapi import FastAPI, APIRouter
from app.utils.sse import sse_manager


router = APIRouter()

@router.get("/api/sse")
async def sse_endpoint():
    return await sse_manager.sse_endpoint()