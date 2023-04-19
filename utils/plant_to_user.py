from models.user_model import UserBase


async def add_plant_to_user(id):
    user = await UserBase.get(id)
    print(user.plants)
