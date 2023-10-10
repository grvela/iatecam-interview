from typing import Union

from fastapi import FastAPI
from app.routers import tag, auth, output, storage, analytics, sse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(analytics.router)
app.include_router(tag.router)
app.include_router(output.router)
app.include_router(storage.router)
app.include_router(sse.router)