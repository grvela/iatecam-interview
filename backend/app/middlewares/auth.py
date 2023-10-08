from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from app.utils.jwt import JWTManager

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    if not JWTManager().verify_token(token):
        raise HTTPException(status_code=401, detail="Unauthorized token")
    payload = JWTManager().decode_token(token)
    return payload