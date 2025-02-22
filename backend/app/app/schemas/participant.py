from typing import Optional, Dict
from datetime import datetime
from pydantic import BaseModel, validator, EmailStr, field_validator, Field
from app.schemas.role import Role
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
import re
from app.schemas.user import User
from app.schemas.project import Project

class ParticipantBase(BaseModel):
    project_id: int = Field(..., description="")
    user_id: int = Field(..., description="")

    created_at: datetime = Field(..., description="")
    updated_at: datetime = Field(..., description="")


# Properties to receive via API on creation
class ParticipantCreate( ParticipantBase):
    ...


# Properties to receive via API on update
class ParticipantUpdate( ParticipantBase):
    ...


class ParticipantInDBBase( ParticipantBase):
    id: Optional[int] = Field(description="", default=None)

    class Config:
        # orm_mode = True
        from_attributes = True


# Additional properties to return via API
class Participant(ParticipantInDBBase):
    project: Project
    user: User

