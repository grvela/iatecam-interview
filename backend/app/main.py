from typing import Union

from fastapi import FastAPI
from app.routers import tag, user, auth, output, product, storage, sales_by_tag, sales_by_product
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
app.include_router(user.router)
app.include_router(sales_by_tag.router)
app.include_router(sales_by_product.router)
app.include_router(tag.router)
app.include_router(output.router)
app.include_router(storage.router)
