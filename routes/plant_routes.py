from fastapi import APIRouter, Depends, Query
from models.user_model import UserBase
from controllers.plants_controllers import add_plant_image
from utils.current_user import get_current_active_user


plant_router = APIRouter()


@plant_router.post("/add-image/")
async def add_one_image(
    plant_id: str,
    path: str = Query(..., description="Path to local file"),
    current_user: UserBase = Depends(get_current_active_user),
):
    await add_plant_image(plant_id, path, current_user)
    return current_user.plants
