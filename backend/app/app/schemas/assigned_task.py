from typing import Optional, Dict
from datetime import datetime
from pydantic import BaseModel, validator, EmailStr, field_validator, Field
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
import re
from app.schemas.user import User
from app.schemas.task import Task
from app.schemas.task_status import Task_Status


class Assigned_TaskBase(BaseModel):
    task_id: int  = Field(..., description="")
    user_id: int  = Field(..., description="")
    task_status_id: int  = Field(..., description="")
    assigned_at: datetime  = Field(..., description="")
    deadline: datetime  = Field(..., description="")

    

# Properties to receive via API on creation
class Assigned_TaskCreate( Assigned_TaskBase):
    ...


# Properties to receive via API on update
class Assigned_TaskUpdate( Assigned_TaskBase):
    ...


class Assigned_TaskInDBBase( Assigned_TaskBase):
    id: Optional[int] = Field(description="", default=None)
    
    created_at: datetime = Field(..., description="")
    updated_at: datetime = Field(..., description="")

    class Config:
        # orm_mode = True
        from_attributes = True


# Additional properties to return via API
class Assigned_Task(Assigned_TaskInDBBase):
    user: User
    task: Task
    task_status: Task_Status