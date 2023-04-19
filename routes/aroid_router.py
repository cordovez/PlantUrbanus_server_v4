from fastapi import APIRouter, HTTPException, status, Query
from models.aroid_model import AroidMongoDB, AroidOut
from typing import List, Annotated
from beanie import PydanticObjectId

from controllers.aroids_controllers import (get_aroids, get_aroid_by_id,
                                            get_aroid_by_taxon)

aroid_router = APIRouter()


@aroid_router.get('/', status_code=status.HTTP_202_ACCEPTED,
                  summary="List of aroids",
                  response_description="Alphabetical by scientific name",
                  response_model=list[AroidMongoDB]
                  )
async def get_all_aroids(limit: int = 10, skip: int = 0) -> list:
    """ This path has a default limit of 10 aroids returned in alphabetical
    order sorted by scientific name. Additionally you can pass a skip value"""
    aroids = await get_aroids(limit, skip)
    if not aroids:
        return [{"message": "Error"}]
    return aroids


@aroid_router.get('/{id}', status_code=status.HTTP_202_ACCEPTED,
                  summary="Find aroid by id",
                  response_description="Aroid by id",
                  response_model=AroidMongoDB)
async def aroid_by_id(id: str):
    aroid_data = await get_aroid_by_id(id)
    if not aroid_data:
        return {"message": f"Aroid with id: {id} was not found"}
    return aroid_data


@aroid_router.get('/taxon/{taxon_id}', status_code=status.HTTP_202_ACCEPTED,
                  summary="Find aroid by taxon",
                  response_description="Aroid by taxon",
                  response_model=AroidOut)
async def get_by_taxon(taxon_id: str) -> AroidMongoDB:
    aroid_data = await get_aroid_by_taxon(taxon_id)

    if not aroid_data:
        return [{"message": "Error"}]
    return aroid_data
