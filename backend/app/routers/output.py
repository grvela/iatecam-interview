from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.services.output import OutputService
from app.schemas.output import Output, CreateOutput, UpdateOutput
from typing import List

router = APIRouter(
    prefix="/outputs",
    tags=["Outputs"]
)

@router.post("/", response_model=Output)
def create_output(output_data: CreateOutput, db: Session = Depends(get_db)):
    return OutputService(db).create_output(output_data)

@router.get("/{output_id}", response_model=Output)
def get_output(output_id: int, db: Session = Depends(get_db)):
    return OutputService(db).get_output(output_id)

@router.put("/{output_id}", response_model=Output)
def update_output(output_id: int, output_data: UpdateOutput, db: Session = Depends(get_db)):
    return OutputService(db).update_output(output_id, output_data)

@router.delete("/{output_id}")
def delete_output(output_id: int, db: Session = Depends(get_db)):
    return OutputService(db).delete_output(output_id)

@router.get("/", response_model=List[Output])
def read_all_outputs(db: Session = Depends(get_db)):
    return OutputService(db).get_all_outputs()
