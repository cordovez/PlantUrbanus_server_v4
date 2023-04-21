from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, Depends, HTTPException, status, Response
from pydantic import EmailStr
from beanie import Link, WriteRules


import logging

from models.user_model import UserIn, UserOut, UserBase
from models.plant_model import PlantMongoDB
from utils.password_hasher import get_password_hash
from utils.cloudinary_upload import uploadImage


async def create_user(user: UserIn):
    """Creates a new user:
    Verifies that neither email nor username already exist in db
    Passes those params and password to a function add_params()
    Saves the returned object from add_params() to the db
    """

    user_email = await UserBase.find_one({"email": user.email})
    user_username = await UserBase.find_one({"username": user.username})

    if user_email is not None:
        raise HTTPException(
            status.HTTP_409_CONFLICT, detail="user with that email already exists"
        )
    if user_username is not None:
        raise HTTPException(
            status.HTTP_409_CONFLICT, detail="user with that username already exists"
        )

    register_user = add_params(user)

    saved_user = await UserBase.create(register_user)
    return saved_user


def add_params(user_in: UserIn):
    """Adds the parameters passed to a user model:
    Makes hash of the plain-text password
    Turns the pydantic user_in into a dict(), without the password
    adds email, username and a newly-created password_hash to a UserBase model
    returns the model
    """
    hashed_password = get_password_hash(user_in.password)
    user_dict = user_in.dict(exclude={"password"})
    user = UserBase(
        email=user_dict["email"],
        username=user_dict["username"],
        password_hash=hashed_password,
    )
    return user


async def get_user(id: str):
    user_data = await UserBase.get(id)
    if not user_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user_data


async def get_users():
    all_users = await UserBase.find().to_list()
    return all_users


async def update_user_data(id: str, user_update_data):
    found_user = await UserBase.get(id)
    update_data = user_update_data.dict(exclude_unset=True)

    updated_item = found_user.copy(update=update_data, exclude={"id"})
    updated_to_json = jsonable_encoder(updated_item)

    update_mongo_doc = await found_user.set({**updated_to_json})

    return True


async def delete_user_by_id(id: str):
    found_user = await UserBase.get(id)
    deleted = await found_user.delete()
    if not deleted:
        return False

    return True


async def add_plant_to_user(path_to_image, user):
    """
    you may need to change the type of new_plant.id to a Link[PlantMongoDB] object, which is a valid reference to a PlantMongoDB object in the UserBase model. You can do this by using the Link function from the bson module to create a new Link object from the new_plant instance
    """
    # Upload to Cloudinary
    file_info = uploadImage(path_to_image)

    # Create new plant with the Plant model and pass values from the Cloudinary upload:
    new_plant = PlantMongoDB(images=[{**file_info}], owner=user.username)

    # insert the new plant to mongodb
    await new_plant.create()

    # add new plant to the current user
    user.plants.append(new_plant)

    await user.save()

    return user.plants
