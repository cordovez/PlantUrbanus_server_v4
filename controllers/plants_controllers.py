from fastapi import FastAPI, File, UploadFile

from typing import Annotated

from models.plant_model import PlantIn, PlantMongoDB


async def add_plant(new_plant: PlantIn):
    """Creates a new plant:"""
    new_plant = await PlantMongoDB.create(new_plant)
    return new_plant
