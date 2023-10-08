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
def create_output(output_data: CreateOutput, db: Session = Depends(get_db)):
    return OutputService(db).create_output(output_data)

@router.get("/me", response_model=List[Output])
def get_all_user_outputs(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return OutputService(db).get_all_outputs_by_user_id(current_user["user_id"])

#TODO 
# @router.get("/last-sells", response_model=List[Output])
# def get_last_sells(db: Session = Depends(get_db)):
#     return OutputService(db).get_all_outputs()

@router.get("/{output_id}", response_model=Output)
def get_output(output_id: int, db: Session = Depends(get_db)):
    return OutputService(db).get_output_(output_id)

@router.delete("/{output_id}")
def delete_output(output_id: int, db: Session = Depends(get_db)):
    return OutputService(db).delete_output(output_id)

@router.get("/", response_model=List[Output])
def read_all_outputs(db: Session = Depends(get_db)):
    return OutputService(db).get_all_outputs()
