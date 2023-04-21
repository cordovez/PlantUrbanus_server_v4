"""
User registration router
"""

from fastapi import APIRouter, Body, Depends, HTTPException, status, Response, Query
from pydantic import EmailStr

from models.user_model import UserIn, UserOut, UserBase, UserUpdate
from models.plant_model import PlantMongoDB
from utils.current_user import get_current_active_user


from controllers.user_controllers import (
    create_user,
    get_user,
    get_users,
    update_user_data,
    delete_user_by_id,
    add_plant_to_user,
)

admin_router = APIRouter()


# Create
# Read
# User by Id
@admin_router.get(
    "/user/{id}",
    response_description="A single document from database",
    response_model=UserBase,
)
async def get_user_by_id(
    id: str, current_user: UserBase = Depends(get_current_active_user)
):
    """Finds a sinlge user by id"""
    if current_user.username != "cordovez":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    user_data = await get_user(id)
    if not user_data:
        return {"message": f"User with id: {id} was not found"}
    return user_data


# All users
@admin_router.get(
    "/users",
    status_code=status.HTTP_202_ACCEPTED,
    summary="List all users",
    response_description="Lists all users",
    response_model=list[UserBase],
)
async def get_all_users(current_user: UserBase = Depends(get_current_active_user)):
    """An unfiltered list of all the users in the database"""
    if current_user.username != "cordovez":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    users = await get_users()
    return users


# All Plants
@admin_router.get("/plants")
async def get_all_plants():
    plants = await PlantMongoDB.find().to_list()
    return plants


# Update
@admin_router.patch(
    "/user/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update a single user",
    response_description="User was updated",
    # response_model=dict,
)
async def update_user(
    id: str,
    user_update_data: UserUpdate,
    current_user: UserBase = Depends(get_current_active_user),
):
    if current_user.username != "cordovez":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    response = await update_user_data(id, user_update_data)
    if response:
        return {"message": "user updated successfully"}
    else:
        return {"message": "user update failed"}


# Delete
@admin_router.delete(
    "/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    # summary="Deletes a single user document from database",
    response_description="Delete a single document from database",
    response_model=dict,
)
async def delete_user(
    id: str, current_user: UserBase = Depends(get_current_active_user)
):
    """Finds a sinlge user by id"""
    if current_user.username != "cordovez":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    delete = await delete_user_by_id(id)

    if not delete:
        return {"message": f"User with id: {id} was not found"}
    else:
        return {"message": f"User with id: {id} was deleted"}
