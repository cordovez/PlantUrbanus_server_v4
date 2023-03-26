from beanie import Document
from datetime import datetime
from pydantic import Field, BaseModel
from typing import Optional
from bson import ObjectId


class Aroid(Document):
    taxon_id: Optional[str] = Field(alias='taxonID')
    scientific_name: Optional[str] = Field(alias='scientificName')
    taxon_rank: Optional[str] = Field(alias='taxonRank')
    family: Optional[str]
    subfamily: Optional[str] | None = None
    references:  Optional[str] | None = None

    class Settings:
        name = "Aroids"

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example":  {
                "_id": "ObjectId",
                "taxon_id": "wfo-0001315076",
                "scientific_name": "Amorphophallus perrieri",
                "taxon_rank": "species",
                "family": "Araceae",
                "subfamily": "null",
                "references": "https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:77142851-1"}
        }
