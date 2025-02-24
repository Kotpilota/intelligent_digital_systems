from typing import Optional, Dict
from datetime import datetime
from pydantic import BaseModel, validator, EmailStr, field_validator, Field
from app.schemas.role import Role
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
import re


class Employment_TypeBase(BaseModel):
    type: str = Field(..., description="")

    

# Properties to receive via API on creation
class Employment_TypeCreate( Employment_TypeBase):
    ...


# Properties to receive via API on update
class Employment_TypeUpdate( Employment_TypeBase):
    ...


class Employment_TypeInDBBase( Employment_TypeBase):
    id: Optional[int] = Field(description="", default=None)

    created_at: datetime = Field(..., description="")
    updated_at: datetime = Field(..., description="")

    class Config:
        # orm_mode = True
        from_attributes = True


# Additional properties to return via API
class Employment_Type(Employment_TypeInDBBase):
    pass
