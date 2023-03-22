from beanie import Document
from datetime import datetime
from pydantic import Field


class Task(Document):
    task_content: str = Field(max_length=400)
    is_complete: bool = False
    date_created: datetime

    class Settings:
        name = "Tasks"

    class Config:
        schema_extra = {
            "task_content": "A sample content",
            "is_complete": True,
            "date_created": datetime.now()
        }
