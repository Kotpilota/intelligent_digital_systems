from typing import Optional, Dict
from datetime import datetime
from pydantic import BaseModel, validator, EmailStr, field_validator, Field
from app.schemas.role import Role
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
import re
from app.schemas.job import Job
from app.schemas.file import File

class Job_ApplicationBase(BaseModel):
    fullname: str = Field(..., description="")
    email: str = Field(..., description="")
    phone: str = Field(..., description="")
    letter: str = Field(..., description="")
    job_id: int = Field(..., description="")
    cv_id: int = Field(..., description="")

    created_at: datetime = Field(..., description="")
    updated_at: datetime = Field(..., description="")

# Properties to receive via API on creation
class Job_ApplicationCreate( Job_ApplicationBase):
    ...


# Properties to receive via API on update
class Job_ApplicationUpdate( Job_ApplicationBase):
    ...


class Job_ApplicationInDBBase( Job_ApplicationBase):
    id: Optional[int] = Field(description="", default=None)

    class Config:
        # orm_mode = True
        from_attributes = True


# Additional properties to return via API
class Job_Application(Job_ApplicationInDBBase):
    job: Job
    cv: File
