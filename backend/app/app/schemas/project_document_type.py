from typing import Optional, Dict
from datetime import datetime
from pydantic import BaseModel, validator, EmailStr, field_validator, Field
from app.schemas.role import Role
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
import re


class Project_Document_TypeBase(BaseModel):
    doctype: str = Field(..., description="")

    

# Properties to receive via API on creation
class Project_Document_TypeCreate( Project_Document_TypeBase):
    ...


# Properties to receive via API on update
class Project_Document_TypeUpdate( Project_Document_TypeBase):
    ...


class Project_Document_TypeInDBBase( Project_Document_TypeBase):
    id: Optional[int] = Field(description="", default=None)

    created_at: datetime = Field(..., description="")
    updated_at: datetime = Field(..., description="")
    
    class Config:
        # orm_mode = True
        from_attributes = True


# Additional properties to return via API
class Project_Document_Type(Project_Document_TypeInDBBase):
    pass

