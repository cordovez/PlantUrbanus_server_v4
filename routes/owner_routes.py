# from fastapi import APIRouter
# from models.owner_model import Owner
# from schema.owner_responses import all_owners_response

# from bson import ObjectId
# from config.db import mongo_db

# owner = APIRouter()
# collection = mongo_db["owners"]


# @owner.post("/owners")
# async def create_owner(owner: Owner):
#     new_owner = collection.insert_one(dict(owner))
#     found_owner = all_owners_response(
#         collection.find({"_id": new_owner.inserted_id}))
#     return {"status": "OK", "data": found_owner}


# @owner.get("/owners")
# async def find_all_owners():
#     users = all_owners_response(collection.find())
#     return {"status": "OK", "data": users}


# @owner.get("/owners/{id}")
# async def get_one_owner(id: str):
#     owner = all_owners_response(collection.find({"_id": ObjectId(id)}))
#     return {"status": "Ok", "data": owner}

# # to do, make fields optional so that if field not changed it doesnt change to default


# @owner.put("/owners/{id}")
# async def update_owner(id: str, owner: Owner):
#     collection.find_one_and_update(
#         {"_id": ObjectId(id)}, {"$set": dict(owner)})
#     owner = all_owners_response(collection.find({"_id": ObjectId(id)}))
#     return {"status": "Ok", "data": owner}


# @owner.delete("/{id}")
# async def delete_owner(id: str):
#     collection.find_one_and_delete({"_id": ObjectId(id)})
#     owners = find_all_owners(collection.find())
#     return {"status": "Ok", "data": []}
