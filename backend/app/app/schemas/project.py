from typing import Optional, Dict

from pydantic import BaseModel, validator, EmailStr, field_validator, Field
from app.schemas.role import Role
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
import re
from datetime import datetime

class ProjectBase(BaseModel):
    name: str = Field(..., description="")
    description: str = Field(..., description="")
    started_at: datetime 
    deadline: datetime 

    


    

# Properties to receive via API on creation
class ProjectCreate( ProjectBase):
    ...


# Properties to receive via API on update
class ProjectUpdate( ProjectBase):
    ...


class ProjectInDBBase( ProjectBase):
    id: Optional[int] = Field(description="", default=None)

    created_at: datetime = Field(..., description="")
    updated_at: datetime = Field(..., description="")
    
    class Config:
        # orm_mode = True
        from_attributes = True

        json_encoders = {
            datetime: lambda dt: dt.strftime("%d-%m-%Y %H:%M")
        }


# Additional properties to return via API
class Project(ProjectInDBBase):
    pass

