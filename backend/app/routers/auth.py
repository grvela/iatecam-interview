from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from typing import Annotated

from app.schemas.auth import LoginUser, RegisterUser

from app.config.database import get_db

from app.services.auth import AuthService
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user_data = LoginUser(username=form_data.username, password=form_data.password)
    return AuthService(db).login_user(user_data)

@router.post("/register")
def register(user: RegisterUser, db: Session = Depends(get_db)):
    pass