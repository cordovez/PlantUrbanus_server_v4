"""
User Models
"""

from datetime import datetime
from typing import Optional


from beanie import Document, Indexed, Link
from pydantic import BaseModel, EmailStr
from passlib.hash import bcrypt

from models.plant_model import PlantMongoDB


class UserBase(Document):
    """User database representation"""

    first_name: Optional[str]
    last_name: Optional[str]
    # plants: list[PlantMongoDB] = [] # dont know why this returns a ValidationError: 1 validation error for UserBase plants -> 0 value is not a valid dict (type=type_error.dict)
    plants: list[Link[PlantMongoDB]] = []
    avatar: Optional[str]
    created_at: Optional[datetime] = datetime.now()
    disabled: bool = False
    email: Optional[EmailStr] | None = None
    username: Optional[str] | None = None
    password_hash: Optional[str] | None = None

    class Settings:
        name = "Users"


class UserIn(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserOut(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    plants: Optional[list]
    avatar: Optional[str]
    email: EmailStr
    username: str


class UserUpdate(BaseModel):
    """User database representation"""

    first_name: Optional[str] | None = None
    last_name: Optional[str] | None = None
    avatar: Optional[str] | None = None
    email: Optional[EmailStr] | None = None
    username: Optional[str] | None = None
