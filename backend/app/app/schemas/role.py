from typing import Optional, ClassVar, Dict

from pydantic import BaseModel, validator, field_validator, Field
from datetime import datetime
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder


class RoleBase(BaseModel):
    # name: ClassVar[str]  = Field(..., description="")
    name: Optional[str] = Field(..., description="")




# Properties to receive via API on creation
class RoleCreate(RoleBase):
    ...
    '''
    @field_validator("name")
    def validate_schema_role(cls, value):
        """Verify the value of role"""
        if value != "employee" and value != "teamlead" and value != "admin" and value != "ceo":
            raise HTTPException(status_code=404, detail="The role differs from allowed")
        return value
    '''

# Properties to receive via API on update
class RoleUpdate(RoleBase):
    ...


class RoleInDBBase(RoleBase):
    id: Optional[int] = Field(description="", default=None)

    created_at: datetime = Field(..., description="")
    updated_at: datetime = Field(..., description="")

    class Config:
        # orm_mode = True
        from_attributes = True


# Additional properties to return via API
class Role(RoleInDBBase):
    pass
