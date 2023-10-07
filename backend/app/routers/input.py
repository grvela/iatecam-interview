from fastapi import APIRouter, Depends, HTTPException, Path, Response
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.services.input import InputService
from app.schemas.input import Input, CreateInput, UpdateInput
from typing import List

router = APIRouter(
    prefix="/inputs",
    tags=["Inputs"]
)

@router.post("/", response_model=Input)
def create_input(input_data: CreateInput, db: Session = Depends(get_db)):
    return InputService(db).create_input(input_data)

@router.get("/{input_id}", response_model=Input)
def get_input(input_id: int, db: Session = Depends(get_db)):
    return InputService(db).get_input(input_id)

@router.put("/{input_id}", response_model=Input)
def update_input(input_id: int, input_data: UpdateInput, db: Session = Depends(get_db)):
    return InputService(db).update_input(input_id, input_data)

@router.delete("/{input_id}")
def delete_input(input_id: int, db: Session = Depends(get_db)):
    return InputService(db).delete_input(input_id)

@router.get("/", response_model=List[Input])
def read_all_inputs(db: Session = Depends(get_db)):
    return InputService(db).get_all_inputs()
