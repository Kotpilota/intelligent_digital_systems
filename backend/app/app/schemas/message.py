from typing import Optional, Dict
from datetime import datetime
from pydantic import BaseModel, validator, EmailStr, field_validator, Field
from app.schemas.role import Role
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
import re
from app.schemas.user import User

class MessageBase(BaseModel):
    sender_id: int = Field(..., description="")
    recipient_id: int = Field(..., description="")
    content: str = Field(..., description="")

    created_at: datetime = Field(..., description="")
    updated_at: datetime = Field(..., description="")

# Properties to receive via API on creation
class MessageCreate( MessageBase):
    ...


# Properties to receive via API on update
class MessageUpdate( MessageBase):
    ...


class MessageInDBBase( MessageBase):
    id: Optional[int] = Field(description="", default=None)

    class Config:
        # orm_mode = True
        from_attributes = True


# Additional properties to return via API
class Message(MessageInDBBase):
    sender: User
    recipient: User

