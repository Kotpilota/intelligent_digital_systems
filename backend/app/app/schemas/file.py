from typing import Optional, Dict
from datetime import datetime
from pydantic import BaseModel, validator, EmailStr, field_validator, Field
from app.schemas.role import Role
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
import re


class FileBase(BaseModel):
    path: str = Field(..., description="")

    created_at: datetime = Field(..., description="")
    updated_at: datetime = Field(..., description="")


# Properties to receive via API on creation
class FileCreate( FileBase):
    ...


# Properties to receive via API on update
class FileUpdate( FileBase):
    ...


class FileInDBBase( FileBase):
    id: Optional[int] = Field(description="", default=None)

    class Config:
        # orm_mode = True
        from_attributes = True


# Additional properties to return via API
class File(FileInDBBase):
    pass
