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
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    return UserService(db).create_user(user)

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return UserService(db).get_user_by_id(user_id)

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user: UpdateUser, db: Session = Depends(get_db)):
    return UserService(db).update_user_by_id(user_id, user)

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return UserService(db).delete_user_by_id(user_id)

@router.get("/", response_model=List[User])
def get_all_users(db: Session = Depends(get_db)):
    return UserService(db).get_all_users()
