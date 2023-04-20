from fastapi import FastAPI, File, UploadFile
from typing import Annotated

from models.plant_model import PlantIn, PlantMongoDB
from models.user_model import UserBase

from utils.cloudinary_upload import uploadImage


# Update: add photo to plant images list


async def add_plant_image(plant_id, path, user):
    plant = next((p for p in user.plants if str(p.id) == plant_id), None)

    # Upload to Cloudinary
    file_info = uploadImage(path)
    plant.images.append(file_info)

    await user.save()
    return True
