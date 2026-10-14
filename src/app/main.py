from fastapi import FastAPI
from app.routers import apply
from fastapi.staticfiles import StaticFiles
from app.routers import admin_menu

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(apply.router)
app.include_router(admin_menu.router)