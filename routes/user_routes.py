from fastapi import APIRouter
from models.user_model import User
from schema.user_schema import users_serializer
from bson import ObjectId
from config.db import mongo_db

user = APIRouter()
collection = mongo_db["users"]


@user.post("/")
async def create_user(user: User):
    new_user = collection.insert_one(dict(user))
    found_user = users_serializer(
        collection.find({"_id": new_user.inserted_id}))
    return {"status": "OK", "data": found_user}


@user.get("/")
async def find_all_users():
    users = users_serializer(collection.find())
    return {"status": "OK", "data": users}


@user.get("/{id}")
async def get_one_user(id: str):
    user = users_serializer(collection.find({"_id": ObjectId(id)}))
    return {"status": "Ok", "data": user}


@user.put("/{id}")
async def update_user(id: str, user: User):
    collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    user = users_serializer(collection.find({"_id": ObjectId(id)}))
    return {"status": "Ok", "data": user}


@user.delete("/{id}")
async def delete_user(id: str):
    collection.find_one_and_delete({"_id": ObjectId(id)})
    users = users_serializer(collection.find())
    return {"status": "Ok", "data": []}
