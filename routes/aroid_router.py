from fastapi import APIRouter, HTTPException
from models.aroid_model import Aroid
from typing import List
from beanie import PydanticObjectId

aroid_router = APIRouter()


@aroid_router.get('/')
async def get_all_aroids() -> list[Aroid]:
    aroids = await Aroid().find_all().to_list()

    return aroids


@aroid_router.post('/')
async def create_aroid(aroid: Aroid) -> dict:
    await aroid.create()
    return {"message": "aroid has been added"}


@aroid_router.post('/add_many')
async def add_aroid_list(aroids: List[Aroid]) -> dict:
    result = await Aroid.insert_many(aroids)
    return {"message": "a list of aroids has been added"}


@aroid_router.get('/{aroid_id}')
async def get_owner_by_id(aroid_id: PydanticObjectId) -> Aroid:
    aroid_by_object_id = await Aroid.get(aroid_id)
    return aroid_by_object_id


@aroid_router.get('taxon/{taxon_id}')
async def get_aroid_by_taxon(taxon_id: str) -> Aroid:
    aroid_by_taxon = await Aroid.find_one({Aroid.taxon_id: taxon_id})
    return aroid_by_taxon
