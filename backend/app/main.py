from typing import Union

from fastapi import FastAPI
from app.routers import tag, user

app = FastAPI()

app.include_router(user.router)
app.include_router(tag.router)