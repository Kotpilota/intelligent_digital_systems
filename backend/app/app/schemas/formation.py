from typing import Optional, Dict

from pydantic import BaseModel, validator, EmailStr, field_validator, Field
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
import re
from app.schemas.user import User


class FormationBase(BaseModel):

    university: str = Field(..., description="")
    faculty: str = Field(..., description="")
    speciality: str = Field(..., description="")
    started_at: datetime = Field(..., description="")
    ended_at: datetime = Field(..., description="")
    user_id: int = Field(..., description="")

    

# Properties to receive via API on creation
class FormationCreate( FormationBase):
    ...


# Properties to receive via API on update
class FormationUpdate( FormationBase):
    ...


class FormationInDBBase( FormationBase):
    id: Optional[int] = Field(description="", default=None)

    created_at: datetime = Field(..., description="")
    updated_at: datetime = Field(..., description="")

    class Config:
        # orm_mode = True
        from_attributes = True


# Additional properties to return via API
class Formation(FormationInDBBase):
    user: User
