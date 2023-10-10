from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.services.output import OutputService
from app.schemas.output import Output, CreateOutput
from typing import List
from app.middlewares.auth import get_current_user

router = APIRouter(
    prefix="/outputs",
    tags=["Outputs"]
)

@router.post("/", response_model=Output)
def create_output(output_data: CreateOutput, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return OutputService(db).create_output(current_user["user_id"], output_data)

@router.get("/latest-sales", response_model=List[Output])
def get_last_sells(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return OutputService(db).get_last_sells()
