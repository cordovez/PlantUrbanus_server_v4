
from models.plant_model import PlantMongoDB
from fastapi.encoders import jsonable_encoder

from utils.cloudinary_upload import uploadImage


async def add_plant_image(plant_id, path, user):
    """
    This function first retrieves the plant document using the get method 
    provided by Beanie. If the plant document is not found, it returns False. 
    Otherwise, it updates the plant document with the new image and saves it.

    Then, it iterates through the user's plant list to find the plant with the 
    specified plant_id, and appends the new image to its image list. Finally, it 
    saves the user document.

    This approach ensures that both the plant document and the user document are 
    updated in a single transaction, so that they remain consistent.
    """
    plant = await PlantMongoDB.get(plant_id)
    if plant is None:
        return False

    # Upload to Cloudinary
    file_info = uploadImage(path)
    plant.images.append(file_info)
    await plant.save()

    return True

async def get_plant_by_id(plant_id, user):
    plant = await PlantMongoDB.get(plant_id)
    return plant
    

async def update_plant_data(plant_id, plant_update_data):
    update_data = plant_update_data.dict(exclude_unset=True)
    plant = await PlantMongoDB.get(plant_id)
    
    updated_plant = plant.copy(update=update_data, exclude={"id"})
    updated_to_json = jsonable_encoder(updated_plant)
    await plant.set({**updated_to_json})
    
    return True


async def delete_plant_by_id(id: str):
    found_plant = await PlantMongoDB.get(id)
    deleted = await found_plant.delete()
    if not deleted:
        return False

    return True