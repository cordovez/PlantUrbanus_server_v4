from fastapi import FastAPI
from routes.owner_router import owner_router
from routes.aroid_router import aroid_router
from routes.user_register import user_router
# from tasks import task_router
from config.db import init_db
import uvicorn


app = FastAPI()
app.include_router(owner_router, prefix='/owners')
app.include_router(aroid_router, prefix='/aroids')
app.include_router(user_router, prefix='/users')


@app.get('/')
def root():
    return "Welcome to PlantUrbanus"


@app.on_event('startup')
async def connect():
    await init_db()


if __name__ == "__main__":
    uvicorn.run(
        reload=True,
        app="main:app"
    )
