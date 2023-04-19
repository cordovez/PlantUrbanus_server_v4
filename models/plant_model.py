# from pydantic import BaseModel, Field, root_validator
# from datetime import datetime
# from typing import Any, List, Optional
# from bson impo

from beanie import Document
from datetime import datetime
from pydantic import Field, BaseModel
from typing import Optional


class PlantIn(BaseModel):
    public_id: str
    uri: str


class PlantMongoDB(Document):
    common_name: Optional[str] | None = None
    scientific_name: Optional[str] | None = None
    images: list[PlantIn] = []
    # public_id: str
    # uri: str
    created_at: Optional[datetime] | None = None

    class Settings:
        name = "Plants"

    class Config:
        schema_extra = {
            "common_name": "Monstera Swiss Cheese",
            "scientific_name": "Monstera deliciosa",
            "images": [
                {
                    "public_id": "PlantUrbanus/fixdbpsl2q7n6klkky0w1",
                    "uri": "https://res.cloudinary.com/database/image/upload/v1/PlantUrbanus/fixdbpsl2q7n6klkky0w1",
                },
            ],
            "date_created": datetime.now(),
        }
