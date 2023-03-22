# from pydantic import BaseModel, Field, root_validator
# from datetime import datetime
# from typing import Any, List, Optional
# from bson import ObjectId


# class Plant(BaseModel):
#     common_name: str | None = None
#     scientific_name: str | None = None
#     created_at: datetime = datetime.now()
#     updated_at: datetime = datetime.now()
#     # owner: ObjectId
#     # owner: str

#     class Config:
#         schema_extra = {
#             "plant_demo": {
#                 "common_name": "Ficus",
#                 "scientific_name": "Ficus Longifoglia",
#                 "owner": '641afb4129eb283b2807a65c'

#             }
#         }
#         validate_assignment = True
#         arbitrary_types_allowed = True

#     @root_validator
#     def date_validator(cls, values):
#         values["updatedAt"] = datetime.now()
#         return values
from beanie import Document
from datetime import datetime
from pydantic import Field


class Plant(Document):
    common_name: str
    scientific_name: str = Field(default=None)
    images: list[str] = []
    date_created: datetime

    class Settings:
        name = "Plants"

    class Config:
        schema_extra = {
            "common_name": "Monstera Swiss Cheese",
            "scientific_name": "Monstera deliciosa",
            "images": ["public_id", "public_id", "public_id"],
            "date_created": datetime.now()
        }
