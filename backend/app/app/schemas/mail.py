from pydantic import BaseModel, Field
from typing import Optional
# from fastapi.encoders import jsonable_encoder
from datetime import datetime


class MailBase(BaseModel):
    name: str = Field(..., description='')
    phone: str = Field(..., description='')
    mail: str = Field(..., description='')
    description: str = Field(..., description='')
    file_path: str = Field(..., description='')
    

class MailCreate(MailBase):
    pass


class MailUpdate(MailBase):
    ...


class MailInDBBase(MailBase):
    id: Optional[int] = Field(description='', default=None)
    created_at: datetime = Field(..., description='')
    updated_at: datetime = Field(..., description='')
    
    class Config:
        from_attributes = True


class Mail(MailInDBBase):
    ...

