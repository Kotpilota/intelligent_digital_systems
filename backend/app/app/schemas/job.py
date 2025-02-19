from typing import Optional, Dict

from pydantic import BaseModel, validator, EmailStr, field_validator, Field
from app.schemas.role import Role
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
import re
from app.schemas.employment_level import Employment_Level
from app.schemas.employment_type import Employment_Type
from app.schemas.location import Location

class JobBase(BaseModel):

    position: str = Field(..., description="")
    description: str = Field(..., description="")
    company: str = Field(..., description="")
    salary: int = Field(..., description="")
    employment_level_id: int = Field(..., description="")
    employment_type_id: int = Field(..., description="")
    location_id: int = Field(..., description="")


# Properties to receive via API on creation
class JobCreate( JobBase):
    ...


# Properties to receive via API on update
class JobUpdate( JobBase):
    ...


class JobInDBBase( JobBase):
    id: Optional[int] = Field(description="", default=None)

    class Config:
        # orm_mode = True
        from_attributes = True


# Additional properties to return via API
class Job(JobInDBBase):
    employment_level: Employment_Level
    employment_type: Employment_Type
    location: Location
