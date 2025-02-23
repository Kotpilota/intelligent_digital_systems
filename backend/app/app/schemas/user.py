from typing import Optional, Dict
from datetime import datetime

from pydantic import BaseModel, validator, EmailStr, field_validator, Field
from app.schemas.role import Role
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
import re


class UserBase(BaseModel):
    nickname: Optional[str]  = Field(..., description="")
    firstname: Optional[str] = Field(default="", description="")
    lastname: Optional[str] = Field(default="", description="")
    hashed_password: Optional[str]  = Field(..., description="")
    email: Optional[str]  = Field(default="", description="")
    phone: Optional[str] = Field(..., description="")
    activated: Optional[bool]  = Field(..., description="")
    role_id: Optional[int]  = Field(..., description="")

    created_at: datetime = Field(..., description="")
    updated_at: datetime = Field(..., description="")


# Properties to receive via API on creation
class UserCreate(UserBase):
    ...
    '''
    @field_validator("phone")
    def phone_validation(cls, v):
        regex = r"^(\+)[1-9][0-9]{9,15}$"
        if v and not re.search(regex, v, re.I):
            raise HTTPException(status_code=400, detail="Phone Number Invalid.")
        return v
    '''

class UserRegister(BaseModel):
    nickname: str  = Field(..., description="")
    phone: str  = Field(..., description="")
    password: str  = Field(..., description="")
    password_check: str = Field(..., description="")
    activated : bool = Field( description="", default=True)
    role_id: int = Field(description="", default=1)

    @field_validator("phone")
    def phone_validation(cls, v):
        regex = r"^(\+)[1-9][0-9]{9,15}$"
        if v and not re.search(regex, v, re.I):
            raise HTTPException(status_code=400, detail="Phone Number Invalid.")
        return v


# Properties to receive via API on update
class UserUpdate(UserBase):
    ...


class UserInDBBase(UserBase):
    id: Optional[int] = Field(description="", default=None)

    class Config:
        # orm_mode = True
        from_attributes = True


# Additional properties to return via API
class User(UserInDBBase):

    role: Role

    @field_validator("role")
    def validate_schema_role(cls, value):
        """Convert to dict if it is a Role object."""
        if value and not isinstance(value, dict):
            return jsonable_encoder(value)
        return value


