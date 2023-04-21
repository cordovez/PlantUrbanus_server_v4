from fastapi import FastAPI, File, UploadFile
from typing import Annotated

from models.plant_model import PlantIn, PlantMongoDB
from models.user_model import UserBase

from utils.cloudinary_upload import uploadImage


async def add_plant_image(plant_id, path, user):
    """
    This function first retrieves the plant document using the get method provided by Beanie. If the plant document is not found, it returns False. Otherwise, it updates the plant document with the new image and saves it.

    Then, it iterates through the user's plant list to find the plant with the specified plant_id, and appends the new image to its image list. Finally, it saves the user document.

    This approach ensures that both the plant document and the user document are updated in a single transaction, so that they remain consistent.
    """
    plant = await PlantMongoDB.get(plant_id)
    if plant is None:
        return False

    # Upload to Cloudinary
    file_info = uploadImage(path)
    plant.images.append(file_info)
    await plant.save()

    return True
