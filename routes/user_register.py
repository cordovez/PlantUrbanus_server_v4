
"""
User registration router
"""

from fastapi import APIRouter, Body, Depends, HTTPException, Response
# from fastapi_jwt_auth import AuthJWT
from pydantic import EmailStr

from models.user_model import User, UserAuth, UserOut

user_router = APIRouter(tags=["User"])


@user_router.post("", response_model=UserOut)
async def user_registration(user_auth: UserAuth):
    """Creates a new user"""
    user = await User.by_email(user_auth.email)
    if user is not None:
        raise HTTPException(409, "user with that email already exists")
    # hashed =
    user = User(email=user_auth.email, password=user_auth.password)
    await user.create()
    return user
