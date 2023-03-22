from fastapi import FastAPI
# from routes.user_routes import user
from routes.owner_router import owner_router
# from routes.plant_routes import plant
from tasks import task_router
from config.db import init_db
import uvicorn


app = FastAPI()
# app.include_router(user)
app.include_router(owner_router, prefix='/owner')
# app.include_router(plant)
app.include_router(task_router, prefix='/task')


@app.on_event('startup')
async def connect():
    await init_db()


if __name__ == "__main__":
    uvicorn.run(
        reload=True,
        app="main:app"
    )
