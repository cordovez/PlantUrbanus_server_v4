"""
User Models
"""

from datetime import datetime
from typing import Optional

# from passlib.hash import bcrypt

from beanie import Document, Indexed
from pydantic import BaseModel, EmailStr
from passlib.hash import bcrypt

from models.plant_model import PlantMongoDB


class UserBase(Document):
    """User database representation"""

    first_name: Optional[str]
    last_name: Optional[str]
    plants: list[PlantMongoDB] = []
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
    plants: list
    avatar: Optional[str]
    email: Indexed(EmailStr, unique=True)
    username: Indexed(str, unique=True)


class UserUpdate(BaseModel):
    """User database representation"""

    first_name: Optional[str] | None = None
    last_name: Optional[str] | None = None
    avatar: Optional[str] | None = None
    email: Optional[EmailStr] | None = None
    username: Optional[str] | None = None
