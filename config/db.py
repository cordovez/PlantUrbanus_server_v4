import beanie
import motor
import motor.motor_asyncio

from dotenv import dotenv_values
# from pymongo import MongoClient
from models.task_models import Task
from models.owner_model import Owner
from models.plant_model import Plant

env = dotenv_values(".env")


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(env["MONGO_URI"])
    await beanie.init_beanie(
        database=client.PlantUrbanus,
        document_models=[Task, Owner, Plant]

    )
# connection = MongoClient(env["MONGO_URI"])
# db = env["MONGO_DB"]  # PlantUrbanus
# mongo_db = connection[db]
