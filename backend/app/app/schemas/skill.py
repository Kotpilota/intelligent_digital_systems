from typing import Optional, Dict
from datetime import datetime
from pydantic import BaseModel, validator, EmailStr, field_validator, Field
from app.schemas.role import Role
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
import re
from app.schemas.skill_type import  Skill_Type

class SkillBase(BaseModel):
    description: str = Field(..., description="")
    skill_type_id: int = Field(..., description="")

    created_at: datetime = Field(..., description="")
    updated_at: datetime = Field(..., description="")

# Properties to receive via API on creation
class SkillCreate( SkillBase):
    ...


# Properties to receive via API on update
class SkillUpdate( SkillBase):
    ...


class SkillInDBBase( SkillBase):
    id: Optional[int] = Field(description="", default=None)

    class Config:
        # orm_mode = True
        from_attributes = True


# Additional properties to return via API
class Skill(SkillInDBBase):
    skill_type: Skill_Type

