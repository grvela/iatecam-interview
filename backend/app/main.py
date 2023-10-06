from typing import Union

from fastapi import FastAPI
from app.routers import tag

app = FastAPI()

app.include_router(tag.router)