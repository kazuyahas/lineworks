from fastapi import FastAPI
from app.routers import apply
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(apply.router)
