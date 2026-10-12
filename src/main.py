from fastapi import FastAPI
from app.routers import apply

app = FastAPI()

app.include_router(apply.router)
