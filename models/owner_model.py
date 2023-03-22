from pydantic import BaseModel, root_validator
# from typing import Any, List, Optional
from models.plant_model import Plant
from beanie import Document
from datetime import datetime
from pydantic import Field


class Owner(Document):
    user_name: str
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    plants: list[Plant] = []
    avatar: str | None = None
    password: str | None = None
    token: str | None = None
    created_at: datetime
    updated_at: datetime

    @root_validator
    def number_validator(cls, values):
        values["updated_at"] = datetime.now()
        return values

    class Settings:
        name = "Owners"

    class Config:
        validate_assignment = True
        schema_extra = {
            "user_name": "cordovez",
            "first_name": "Juan Carlos",
            "last_name": "Cordovez",
            "email": "cordovez@apple.com",
            "plants": "[id, id, id]",
            "avatar": "string to cloudinary",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
