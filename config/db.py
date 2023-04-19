import beanie
import motor
import motor.motor_asyncio

from dotenv import dotenv_values
# from pymongo import MongoClient
# from models.task_models import Task
from models.user_model import UserBase
from models.aroid_model import AroidMongoDB
from models.plant_model import PlantMongoDB
"""Beanie uses a single model to create database models and give responses, so
models have to be imported into the client initialization.
    """

env = dotenv_values(".env")


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(env["MONGO_URI"])
    await beanie.init_beanie(
        database=client.PlantUrbanus,
        document_models=[AroidMongoDB, UserBase, PlantMongoDB]

    )
