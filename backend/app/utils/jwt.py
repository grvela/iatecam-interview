from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import HTTPException

from app.config.config import get_settings

settings = get_settings()

class JWTManager:
    def __init__(self):
        self.secret_key = settings.SECRET_KEY
        self.algorithm = settings.ALGORITHM
        self.token_expire_minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES

    def create_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=self.token_expire_minutes)
        to_encode.update({"exp": expire})
        token = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return token

    def decode_token(self, token: str) -> dict:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except JWTError as e:
            raise HTTPException(status_code=401, detail="Could not decode token")

    def verify_token(self, token: str) -> bool:
        try:
            payload = self.decode_token(token)
            return True
        except HTTPException:
            return False
