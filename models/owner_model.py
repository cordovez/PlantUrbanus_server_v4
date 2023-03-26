from pydantic import BaseModel, root_validator, validator
# from typing import Any, List, Optional
from models.plant_model import Plant
from beanie import Document
from datetime import datetime
from pydantic import Field
from typing import Optional


class Owner(Document):
    user_name: str
    first_name: Optional[str] | None = None
    last_name: Optional[str] | None = None
    email: str
    plants: list[Plant] = []
    avatar: Optional[str] | None = None
    password: Optional[str] | None = None
    created_at: Optional[datetime] = datetime.now
    created_at: Optional[datetime] | None = None

    # @validator("created_at", pre=True)
    # def check_creation_date(cls, value):
    #     if value != None:
    #         value = value
    #     else:
    #         value = datetime.now()
    #     return value

    # @root_validator(skip_on_failure=True)
    # def set_timestamps(cls, values):
    #     created_at = datetime.now()
    #     updated_at = None
    #     if created_at != None:
    #         updated_at = datetime.now()
    #     values["updated_at"] = updated_at
    #     return values

    class Settings:
        name = "Owners"

    class Config:
        # validate_assignment = True
        schema_extra = {
            "example": {"user_name": "cordovez",
                        "first_name": "Juan Carlos",
                        "last_name": "Cordovez",
                        "email": "cordovez@apple.com",
                        "plants": "[id, id, id]",
                        "avatar": "string to cloudinary",
                        "created_at": "2023-03-23T16:45:25.937968",
                        "updated_at": "2023-03-23T16:45:25.937968"}
        }
