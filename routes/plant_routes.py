# from fastapi import APIRouter
# from models.plant_model import Plant
# from schema.plant_responses import all_plants_response

# from bson import ObjectId
# from config.db import mongo_db

# plant = APIRouter()
# collection = mongo_db["plants"]


# @plant.post("/plants")
# async def create_plant(plant: Plant):
#     new_plant = collection.insert_one(dict(plant))
#     found_plant = all_plants_response(
#         collection.find({"_id": new_plant.inserted_id}))
#     return {"status": "OK", "data": found_plant}


# @plant.get("/plants")
# async def find_all_plants():
#     users = all_plants_response(collection.find())
#     return {"status": "OK", "data": users}


# @plant.get("/plants/{id}")
# async def get_one_user(id: str):
#     plant = all_plants_response(collection.find({"_id": ObjectId(id)}))
#     return {"status": "Ok", "data": plant}

# # to do, make fields optional so that if field not changed it doesnt change to default


# @plant.put("/plants/{id}")
# async def update_plant(id: str, plant: Plant):
#     collection.find_one_and_update(
#         {"_id": ObjectId(id)}, {"$set": dict(plant)})
#     plant = all_plants_response(collection.find({"_id": ObjectId(id)}))
#     return {"status": "Ok", "data": plant}


# @plant.delete("/plants/{id}")
# async def delete_plant(id: str):
#     collection.find_one_and_delete({"_id": ObjectId(id)})
#     plants = find_all_plants(collection.find())
#     return {"status": "Ok", "data": []}
