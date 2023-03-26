from fastapi import APIRouter, HTTPException
from models.owner_model import Owner
from typing import List, Dict
from beanie import PydanticObjectId

owner_router = APIRouter()


@owner_router.get('/', response_model=List[Owner])
async def get_all_owners() -> list[Owner]:
    """
    Returns a list of all owners in the database.
    """
    owners = await Owner.find_all().to_list()

    return owners


@owner_router.post('/', response_model=Owner)
# async def create_owner(owner: Owner) -> Dict[str, str]:
async def create_owner(owner: Owner) -> Owner:
    """
    Creates a new owner in the database. 
    The request body must include 'user_name',  'email' and 'created_at' datetime.

    """
    # check to see if owner already exists
    owner_exists = await Owner.find_one({"email": owner.email})
    if owner_exists:
        raise HTTPException(status_code=400, detail="Owner already exists")
    else:
        created_owner = await owner.create()
        # new_owner = await Owner.get(created_owner.insertedId)
        return created_owner
        # return created_owner


@owner_router.get('/{owner_id}', response_model=Owner)
async def get_owner_by_id(owner_id: PydanticObjectId) -> Owner:
    """find a single owner by _id
    Returns:
        Owner: the owner document object
    """
    found_owner = await Owner.get(owner_id)

    if not found_owner:
        raise HTTPException(status_code=404, detail="Owner not found")

    return found_owner


@owner_router.put('/{owner_id}')
async def update_owner_by_id(owner: Owner, owner_id: PydanticObjectId) -> Owner:
    """
    updates owner document for fields not used for authorisation. 
    'user_name' and 'email' must passed as empty strings until authorization is
    created
    """
    # Get the owner from the database
    owner_to_update = await Owner.get(owner_id)

    if not owner_to_update:
        raise HTTPException(status_code=404, detail="Resource not found")

    # Create a mapping of field names in the Owner model to field names in the MongoDB collection
    owner_to_update.first_name = owner.first_name
    owner_to_update.last_name = owner.last_name
    owner_to_update.plants = owner.plants
    owner_to_update.avatar = owner.avatar

    await owner_to_update.replace()

    # await owner_to_update.refresh()
    return owner_to_update


@owner_router.delete('/{owner_id}')
async def delete_owner(owner_id: PydanticObjectId) -> dict:
    owner_to_delete = await Owner.get(owner_id)

    await owner_to_delete.delete()

    return {"message": "owner deleted"}
