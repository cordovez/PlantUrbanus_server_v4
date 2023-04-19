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

user_router = APIRouter()


# Create
@user_router.post("/create", response_model=UserBase)
async def add_user_to_db(user: UserIn):
    new_user = await create_user(user)
    return new_user


@user_router.post("/me/add-plant")
async def new_plant(
    path: str = Query(..., description="Path to local file"),
    current_user: UserBase = Depends(get_current_active_user),
):
    new_plant = await add_plant_to_user(path, current_user)

    return new_plant


# Read
@user_router.get("/me", response_model=UserBase)
async def read_user_me(current_user: UserBase = Depends(get_current_active_user)):
    return current_user


@user_router.get("/me/plants")
async def read_user_plants(
    current_user: UserBase = Depends(get_current_active_user),
) -> list:
    return current_user.plants


# @user_router.get(
#     "/{id}",
#     response_description="A single document from database",
#     response_model=UserBase,
# )
# async def get_user_by_id(id: str):
#     """Finds a sinlge user by id"""
#     user_data = await get_user(id)
#     if not user_data:
#         return {"message": f"User with id: {id} was not found"}
#     return user_data


# @user_router.get(
#     "/",
#     status_code=status.HTTP_202_ACCEPTED,
#     summary="List all users",
#     response_description="Lists all users",
#     response_model=list[UserBase],
# )
# async def get_all_users():
#     """An unfiltered list of all the users in the database"""
#     users = await get_users()
#     return users


# Update
# To do: change this to patch('/me')
# @user_router.patch(
#     "/{id}",
#     status_code=status.HTTP_202_ACCEPTED,
#     summary="Update a single user",
#     response_description="User was updated",
#     response_model=dict,
# )
# async def update_user(id: str, user_update_data: UserUpdate):
#     response = await update_user_data(id, user_update_data)
#     if response:
#         return {"message": "user updated successfully"}
#     else:
#         return {"message": "user update failed"}


# Delete
# To do: change this to delete("/me")
# @user_router.delete(
#     "/{id}",
#     status_code=status.HTTP_202_ACCEPTED,
#     # summary="Deletes a single user document from database",
#     response_description="Delete a single document from database",
#     response_model=dict,
# )
# async def delete_user(id: str):
#     """Finds a sinlge user by id"""
#     delete = await delete_user_by_id(id)

#     if not delete:
#         return {"message": f"User with id: {id} was not found"}
#     else:
#         return {"message": f"User with id: {id} was deleted"}
