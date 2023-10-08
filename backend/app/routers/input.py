from fastapi import APIRouter, Depends, HTTPException, Path, Response
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.services.input import InputService
from app.schemas.input import Input, CreateInput
from typing import List

from app.middlewares.auth import get_current_user

router = APIRouter(
    prefix="/inputs",
    tags=["Inputs"]
)

@router.post("/", response_model=Input)
def create_input(input_data: CreateInput, db: Session = Depends(get_db)):
    return InputService(db).create_input(input_data)

@router.get("/me", response_model=List[Input])
def get_all_user_inputs(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return InputService(db).get_all_inputs_by_user_id(current_user["user_id"])

@router.get("/{input_id}", response_model=Input)
def get_input(input_id: int, db: Session = Depends(get_db)):
    return InputService(db).get_input(input_id)

@router.delete("/{input_id}")
def delete_input(input_id: int, db: Session = Depends(get_db)):
    return InputService(db).delete_input(input_id)

@router.get("/", response_model=List[Input])
def read_all_inputs(db: Session = Depends(get_db)):
    return InputService(db).get_all_inputs()
