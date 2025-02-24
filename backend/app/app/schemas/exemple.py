from pydantic import BaseModel, HttpUrl, Field
from typing import Sequence, Optional, Dict
from fastapi.encoders import jsonable_encoder
from datetime import datetime

class ExempleBase(BaseModel):
    string_attribute: str  = Field(..., description="")
    integer_attribute: int  = Field(..., description="")
    float_attribute: float  = Field(..., description="")
    boolean_attribute: bool  = Field(..., description="")

    

class ExempleCreate(ExempleBase):
    pass



# Properties to receive via API on update
class ExempleUpdate(ExempleBase):
    ...


class ExempleInDBBase(ExempleBase):
    id: Optional[int] = Field(description="", default=None)

    created_at: datetime = Field(..., description="")
    updated_at: datetime = Field(..., description="")
    
    class Config:
        # orm_mode = True
        from_attributes = True


# Additional properties to return via API
class Exemple(ExempleInDBBase):
    ...

    '''
    @validator("user_type")
    def validate_schema_user_type(cls, value):
        """Convert to dict if it is a User_Type object."""
        if value and not isinstance(value, dict):
            return jsonable_encoder(value)
        return value
    '''