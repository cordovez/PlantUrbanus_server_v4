
from beanie import Document
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class PlantIn(BaseModel):
    public_id: str
    uri: str


class PlantMongoDB(Document):
    common_name: Optional[str] | None = None
    scientific_name: Optional[str] | None = None
    images: Optional[list] = []
    pest_treatment: Optional[str] | None = None
    substrate: Optional[str] | None = None
    nutrients: Optional[str] | None = None
    notes: Optional[str] | None = None
    date_of_purchase: Optional[str] | None = None
    purchased_at: Optional[str] | None = None
    price_paid: Optional[float] | None = None
    owner: Optional[str] | None = None
    created_at: Optional[datetime] = datetime.now()

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


class PlantOut(BaseModel):
    common_name: Optional[str] | None = None
    scientific_name: Optional[str] | None = None
    images: Optional[list] = []
    pest_treatment: Optional[str] | None = None
    substrate: Optional[str] | None = None
    nutrients: Optional[str] | None = None
    notes: Optional[str] | None = None
    date_of_purchase: Optional[str] | None = None
    purchased_at: Optional[str] | None = None
    price_paid: Optional[float] | None = None
    created_at: datetime

class PlantUpdate(BaseModel):
    common_name: Optional[str] | None = None
    scientific_name: Optional[str] | None = None
    pest_treatment: Optional[str] | None = None
    substrate: Optional[str] | None = None
    nutrients: Optional[str] | None = None
    notes: Optional[str] | None = None
    date_of_purchase: Optional[str] | None = None
    purchased_at: Optional[str] | None = None
    price_paid: Optional[float] | None = None