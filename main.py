from fastapi import FastAPI
from routes.user_routes import user
import uvicorn


app = FastAPI()
app.include_router(user)

if __name__ == "__main__":
    uvicorn.run(
        reload=True,
        app="main:app"
    )
