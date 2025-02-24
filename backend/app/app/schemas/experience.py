from typing import Optional, Dict
from datetime import datetime
from pydantic import BaseModel, validator, EmailStr, field_validator, Field
from app.schemas.role import Role
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
import re
from app.schemas.user import User


class ExperienceBase(BaseModel):

    company: str = Field(..., description="")
    position:str = Field(..., description="")
    started_at: datetime = Field(..., description="")
    ended_at: datetime = Field(..., description="")
    user_id: int = Field(..., description="")

    

# Properties to receive via API on creation
class ExperienceCreate( ExperienceBase):
    ...


# Properties to receive via API on update
class ExperienceUpdate( ExperienceBase):
    ...


class ExperienceInDBBase( ExperienceBase):
    id: Optional[int] = Field(description="", default=None)

    created_at: datetime = Field(..., description="")
    updated_at: datetime = Field(..., description="")

    class Config:
        # orm_mode = True
        from_attributes = True


# Additional properties to return via API
class Experience(ExperienceInDBBase):
    user: User
