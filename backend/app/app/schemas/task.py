from typing import Optional, Dict
from datetime import datetime
from pydantic import BaseModel, validator, EmailStr, field_validator, Field
from app.schemas.role import Role
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
import re
from app.schemas.project import Project

class TaskBase(BaseModel):
    name: str= Field(..., description="")
    description: str = Field(..., description="")
    project_id: int = Field(..., description="")

    




# Properties to receive via API on creation
class TaskCreate( TaskBase):
    ...


# Properties to receive via API on update
class TaskUpdate( TaskBase):
    ...


class TaskInDBBase( TaskBase):
    id: Optional[int] = Field(description="", default=None)

    created_at: datetime = Field(..., description="")
    updated_at: datetime = Field(..., description="")
    
    class Config:
        # orm_mode = True
        from_attributes = True


# Additional properties to return via API
class Task(TaskInDBBase):
    project: Project

