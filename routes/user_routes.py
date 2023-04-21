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
@user_router.post("/create")
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
@user_router.get("/me")
async def read_user_me(current_user: UserBase = Depends(get_current_active_user)):
    return current_user


@user_router.get("/me/plants")
async def read_user_plants(
    current_user: UserBase = Depends(get_current_active_user),
):
    return current_user.plants
