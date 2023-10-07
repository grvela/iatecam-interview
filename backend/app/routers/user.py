from fastapi import APIRouter, Depends, HTTPException, Path, Response
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.services.user import UserService
from app.schemas.user import User, CreateUser, UpdateUser
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", response_model=User)
def create_user(user_data: CreateUser, db: Session = Depends(get_db)):
    return UserService(db).create_user(user_data)

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return UserService(db).get_user(user_id)

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user_data: UpdateUser, db: Session = Depends(get_db)):
    return UserService(db).update_user(user_id, user_data)

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return UserService(db).delete_user(user_id)

@router.get("/", response_model=List[User])
def read_all_users(db: Session = Depends(get_db)):
    return UserService(db).get_all_users()
