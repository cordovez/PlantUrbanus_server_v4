from fastapi import APIRouter, Body, Depends, HTTPException, status, Response, Query
from models.plant_model import PlantMongoDB, PlantIn
from models.user_model import UserBase
from controllers.plants_controllers import add_plant_image
from utils.current_user import get_current_active_user

from utils.cloudinary_upload import uploadImage

plant_router = APIRouter()


@plant_router.post("/add-image/")
async def add_one_image(
    plant_id: str,
    path: str = Query(..., description="Path to local file"),
    current_user: UserBase = Depends(get_current_active_user),
):
    new_image = await add_plant_image(plant_id, path, current_user)
    return new_image


@plant_router.get("/")
async def get_all_plants():
    plants = await PlantMongoDB.find().to_list()
    return plants
