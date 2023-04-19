"""
User registration router
"""

from fastapi import APIRouter, Body, Depends, HTTPException, status, Response, Query
from pydantic import EmailStr

from models.user_model import UserIn, UserOut, UserBase, UserUpdate
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
@admin_router.post("/create", response_model=UserBase)
async def add_user_to_db(user: UserIn):
    new_user = await create_user(user)
    return new_user


@admin_router.get(
    "/{id}",
    response_description="A single document from database",
    response_model=UserBase,
)
async def get_user_by_id(id: str):
    """Finds a sinlge user by id"""
    user_data = await get_user(id)
    if not user_data:
        return {"message": f"User with id: {id} was not found"}
    return user_data


@admin_router.get(
    "/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="List all users",
    response_description="Lists all users",
    response_model=list[UserBase],
)
async def get_all_users():
    """An unfiltered list of all the users in the database"""
    users = await get_users()
    return users


# Update
@admin_router.patch(
    "/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update a single user",
    response_description="User was updated",
    # response_model=dict,
)
async def update_user(id: str, user_update_data: UserUpdate):
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
async def delete_user(id: str):
    """Finds a sinlge user by id"""
    delete = await delete_user_by_id(id)

    if not delete:
        return {"message": f"User with id: {id} was not found"}
    else:
        return {"message": f"User with id: {id} was deleted"}
