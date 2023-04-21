from models.aroid_model import AroidMongoDB
from fastapi import status, HTTPException


async def get_aroids(limit, skip):
    aroids = await AroidMongoDB.find().sort("scientificName").limit(limit).skip(skip).to_list()
    return aroids


async def get_aroid_by_id(id: str):
    aroid_data = await AroidMongoDB.get(id)
    if not aroid_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return aroid_data


async def get_aroid_by_taxon(taxon_id: str):
    aroid_data = await AroidMongoDB.find_one({"taxonID": taxon_id})
    return aroid_data
