from typing import Union

from fastapi import FastAPI
from app.routers import tag, user, auth, output, product, storage, input

app = FastAPI()


app.include_router(auth.router)
app.include_router(user.router)
app.include_router(tag.router)
app.include_router(input.router)
app.include_router(output.router)
app.include_router(product.router)
app.include_router(storage.router)
