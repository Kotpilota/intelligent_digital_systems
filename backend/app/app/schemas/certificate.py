from typing import Optional, Dict
from datetime import datetime
from pydantic import BaseModel, validator, EmailStr, field_validator, Field
from app.schemas.role import Role
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
import re
from app.schemas.user import User
from app.schemas.file import File


class CertificateBase(BaseModel):

    user_id: int =  Field(..., description="")
    file_id: int = Field(..., description="")

    

# Properties to receive via API on creation
class CertificateCreate( CertificateBase):
    ...


# Properties to receive via API on update
class CertificateUpdate( CertificateBase):
    ...


class CertificateInDBBase( CertificateBase):
    id: Optional[int] = Field(description="", default=None)

    created_at: datetime = Field(..., description="")
    updated_at: datetime = Field(..., description="")
    
    class Config:
        # orm_mode = True
        from_attributes = True


# Additional properties to return via API
class Certificate(CertificateInDBBase):
    user: User
    file: File
