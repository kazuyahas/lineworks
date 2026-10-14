from fastapi import FastAPI
from app.routers import apply
from fastapi.staticfiles import StaticFiles
from app.routers import admin_menu
from app.services.auth import get_access_token

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# ★ 起動時にアクセストークンをセットする
@app.on_event("startup")
async def startup_event():
    app.state.access_token = get_access_token()
app.include_router(apply.router)
app.include_router(admin_menu.router)