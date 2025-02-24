from typing import Optional, Dict
from datetime import datetime
from pydantic import BaseModel, validator, EmailStr, field_validator, Field
from app.schemas.role import Role
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
import re
from app.schemas.file import File
from app.schemas.project import Project
from app.schemas.project_document_type import Project_Document_Type

class Project_DocumentBase(BaseModel):
    project_id: int = Field(..., description="")
    doctype_id: int = Field(..., description="")
    file_id: int  = Field(..., description="")

    

# Properties to receive via API on creation
class Project_DocumentCreate( Project_DocumentBase):
    ...


# Properties to receive via API on update
class Project_DocumentUpdate( Project_DocumentBase):
    ...


class Project_DocumentInDBBase( Project_DocumentBase):
    id: Optional[int] = Field(description="", default=None)

    created_at: datetime = Field(..., description="")
    updated_at: datetime = Field(..., description="")
    
    class Config:
        # orm_mode = True
        from_attributes = True


# Additional properties to return via API
class Project_Document(Project_DocumentInDBBase):
    project: Project
    doctype: Project_Document_Type
    file: File

