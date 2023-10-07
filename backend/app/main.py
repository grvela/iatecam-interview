from typing import Union

from fastapi import FastAPI
from app.routers import tag, user, auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(tag.router)