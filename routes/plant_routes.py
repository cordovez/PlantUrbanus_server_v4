from fastapi import APIRouter, Depends, Query, HTTPException, status
from models.user_model import UserBase
from models.plant_model import PlantOut, PlantUpdate

from controllers.plants_controllers import (add_plant_image, get_plant_by_id,
update_plant_data, delete_plant_by_id)
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

# @plant_router.get("/user-plants", response_model=list)
# async def get_images(
#     plant_id: str,current_user: UserBase = Depends(get_current_active_user)
# ):
#     results = await get_plant_by_id(plant_id)
    
#     return results
@plant_router.get("/{plant_id}", response_model=PlantOut)
async def get_images(
    plant_id: str, current_user: UserBase = Depends(get_current_active_user)
):
    results = await get_plant_by_id(plant_id, current_user )
    
    return results


@plant_router.patch(
    "/update/{plant_id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update a single plant",
    response_description="Plant was updated",
    # response_model=dict,
)
async def update_plant(
    plant_id: str,
    plant_update_data: PlantUpdate,
    current_user: UserBase = Depends(get_current_active_user),
):
    response = await update_plant_data(plant_id, plant_update_data)
    if response:
        return {"message": "user updated successfully"}
    else:
        return {"message": "user update failed"}


@plant_router.delete("/delete/{plant_id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Delete a single plant",
    response_description="Plant was deleted",)
async def delete_plant(plant_id: str, 
                       current_user: UserBase = 
                       Depends(get_current_active_user) ):
    response = await delete_plant_by_id(plant_id)
    if response:
        return f"Plant with id: {plant_id} was deleted"