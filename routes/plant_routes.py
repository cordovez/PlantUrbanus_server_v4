from fastapi import APIRouter, Body, Depends, HTTPException, status, Response, Query
from models.plant_model import PlantMongoDB, PlantIn
from models.user_model import UserBase
from controllers.plants_controllers import add_plant
from utils.current_user import get_current_active_user

from utils.cloudinary_upload import uploadImage

plant_router = APIRouter()


@plant_router.get("/my-plants")
async def read_users_me(current_user: UserBase = Depends(get_current_active_user)):
    plant_list = current_user.plants
    return plant_list


@plant_router.post("/add/")
async def add_one_image(
    path: str = Query(..., description="Path to local file"),
    current_user: UserBase = Depends(get_current_active_user),
):
    # Upload to Cloudinary
    file_info = uploadImage(path)

    # Create new plant and pass values from the Cloudinary upload:
    new_plant = PlantMongoDB(images=[{**file_info}])

    # insert the new plant to mongodb
    await new_plant.insert()

    # add new plant
    user_plant_list = await current_user.set({UserBase.plants: [new_plant]})

    return user_plant_list


@plant_router.get("/")
async def get_all_plants():
    plants = await PlantMongoDB.find().to_list()
    return plants
