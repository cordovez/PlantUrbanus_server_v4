"""
User registration router
"""

from fastapi import APIRouter, Depends, Query, status

from models.user_model import UserIn, UserBase, UserOut, UserUpdate
from utils.current_user import get_current_active_user
from controllers.user_controllers import update_user_data, add_avatar_image


from controllers.user_controllers import (
    create_user,
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
    public_id, url,
    current_user: UserBase = Depends(get_current_active_user),
):
    try:
        new_plant = await add_plant_to_user(public_id, url, current_user)
        return new_plant
    except Exception as e:
        print(str(e))
        raise e

@user_router.post("/me/add-avatar")
async def create_avatar(
    path: str = Query(..., description="Path to local file"),
    current_user: UserBase = Depends(get_current_active_user),
):
    avatar = await add_avatar_image(path, current_user)

    return avatar

# Read
@user_router.get("/me", response_model=UserOut)
async def read_user_me(current_user: UserBase = Depends(get_current_active_user)):
    user_data = current_user.dict()
    return user_data


@user_router.get("/me/plants")
async def read_user_plants(
    current_user: UserBase = Depends(get_current_active_user),
):
    
    user = await UserBase.get(str(current_user.id), fetch_links=True)
    
    return user.plants

# Update
@user_router.patch(
    "/me/update",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update a single user",
    response_description="User was updated",
    # response_model=dict,
)
async def update_user(
    user_update_data: UserUpdate,
    current_user: UserBase = Depends(get_current_active_user),
):
    response = await update_user_data( current_user, user_update_data)
    if response:
        return {"message": "user updated successfully"}
    else:
        return {"message": "user update failed"}



