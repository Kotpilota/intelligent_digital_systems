from typing import Optional, Dict
from datetime import datetime
from pydantic import BaseModel, validator, EmailStr, field_validator, Field
from app.schemas.role import Role
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
import re
from app.schemas.user import User
from app.schemas.skill import Skill

class Has_SkillBase(BaseModel):

    user_id: Optional[int] = Field(..., description="ID пользователя")
    skill_id: Optional[int] = Field(..., description="ID навыка")

    created_at: datetime = Field(..., description="")
    updated_at: datetime = Field(..., description="")


# Properties to receive via API on creation
class Has_SkillCreate( Has_SkillBase):
    ...


# Properties to receive via API on update
class Has_SkillUpdate( Has_SkillBase):
    ...


class Has_SkillInDBBase( Has_SkillBase):
    id: Optional[int] = Field(description="", default=None)

    class Config:
        # orm_mode = True
        from_attributes = True


# Additional properties to return via API
class Has_Skill(Has_SkillInDBBase):
    user: User
    skill: Skill