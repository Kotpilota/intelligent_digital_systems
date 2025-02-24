from typing import Optional, Dict
from datetime import datetime
from pydantic import BaseModel, validator, EmailStr, field_validator, Field
from app.schemas.role import Role
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
import re


class Task_StatusBase(BaseModel):
    status: str = Field(..., description="")

    


# Properties to receive via API on creation
class Task_StatusCreate( Task_StatusBase):
    ...


# Properties to receive via API on update
class Task_StatusUpdate( Task_StatusBase):
    ...


class Task_StatusInDBBase( Task_StatusBase):
    id: Optional[int] = Field(description="", default=None)

    created_at: datetime = Field(..., description="")
    updated_at: datetime = Field(..., description="")
    
    class Config:
        # orm_mode = True
        from_attributes = True


# Additional properties to return via API
class Task_Status(Task_StatusInDBBase):
    pass

