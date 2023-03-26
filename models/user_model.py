"""
User Models
"""

from datetime import datetime
from typing import Optional

from beanie import Document, Indexed
from pydantic import BaseModel, EmailStr


# Model hierarchy from parents to children

class UserAuth(BaseModel):
    """User registration and login authorisation"""

    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    """Updatable user fields"""

    email: Optional[EmailStr] = None

    # User information
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserOut(UserUpdate):
    """User fields returned to client"""

    email: Indexed(EmailStr, unique=True)
    disabled: bool = False


class User(Document, UserOut):
    """User database representation"""

    password: str
    email_confirmed_at: Optional[datetime] = None

    def __repr__(self) -> str:
        return f"<User {self.email}"

    def __str__(self) -> str:
        return self.email

    # why do we need the hash number?
    def __hash__(self) -> int:
        return hash(self.email)

    # verify that object passed email is same as this User email
    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.email == other.email
        return False

    # an internal way to implement setters and getters
    @property
    def created(self) -> datetime:
        """Datetime user was created from ID"""
        return self.id.generation_time

    @classmethod
    async def by_email(cls, email: str) -> "User":
        """Get a user by email"""
        return await cls.find_one(cls.email == email)

    class Settings:
        name = "Users"
