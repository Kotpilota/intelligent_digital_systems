from typing import Optional, Dict
from datetime import datetime
from pydantic import BaseModel, validator, EmailStr, field_validator, Field
from app.schemas.role import Role
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
import re


class LocationBase(BaseModel):
    city: str = Field(..., description="")
    country: str = Field(..., description="")

    created_at: datetime = Field(..., description="")
    updated_at: datetime = Field(..., description="")

# Properties to receive via API on creation
class LocationCreate( LocationBase):
    ...


# Properties to receive via API on update
class LocationUpdate( LocationBase):
    ...


class LocationInDBBase( LocationBase):
    id: Optional[int] = Field(description="", default=None)

    class Config:
        # orm_mode = True
        from_attributes = True


# Additional properties to return via API
class Location(LocationInDBBase):
    pass

