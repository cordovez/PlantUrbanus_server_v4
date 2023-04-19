from fastapi import FastAPI
from models.tags_models import Tag
from config.db import init_db
import uvicorn

from routes.aroid_router import aroid_router
from routes.user_routes import user_router
from routes.token_router import token_router
from routes.plant_routes import plant_router
from routes.admin_routes import admin_router


app = FastAPI()


@app.get("/", tags=["root"])
def root():
    return "Welcome to PlantUrbanus"


app.include_router(admin_router, prefix="/admin", tags=[Tag.admin])
app.include_router(user_router, prefix="/users", tags=[Tag.users])
app.include_router(plant_router, prefix="/plants", tags=[Tag.plants])
# app.include_router(aroid_router, prefix="/aroids", tags=[Tag.aroids])
app.include_router(token_router, tags=["token"])


@app.on_event("startup")
async def connect():
    await init_db()


if __name__ == "__main__":
    uvicorn.run(reload=True, app="main:app")
