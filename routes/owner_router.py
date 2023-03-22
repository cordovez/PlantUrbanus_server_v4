from fastapi import APIRouter, HTTPException
from models.owner_model import Owner
from typing import List
from beanie import PydanticObjectId

owner_router = APIRouter()


@owner_router.get('/')
async def get_all_owners() -> list[Owner]:
    owners = await Owner.find_all().to_list()

    return owners


@owner_router.post('/')
async def create_owner(owner: Owner):
    await owner.create()
    return {"message": "owner has been saved"}


@owner_router.get('/{owner_id}')
async def get_owner_by_id(owner_id: PydanticObjectId) -> Owner:
    owner_to_get = await Owner.get(owner_id)
    return owner_to_get


@owner_router.put('/{owner_id}')
async def update_owner_by_id(owner: Owner, owner_id: PydanticObjectId) -> Owner:

    owner_to_update = await Owner.get(owner_id)

    if not owner_to_update:
        raise HTTPException(status_code=404, detail="Resource not found")

    owner_to_update.user_name = owner.user_name

    await owner_to_update.save()

    return owner_to_update


@owner_router.delete('/{owner_id}')
async def delete_owner(owner_id: PydanticObjectId):
    owner_to_delete = await Owner.get(owner_id)

    await owner_to_delete.delete()

    return {"message": "owner deleted"}
