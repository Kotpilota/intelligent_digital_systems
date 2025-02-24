from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, List

from app import crud
from app.api import deps
from app.schemas.skill_type import Skill_Type, Skill_TypeCreate, Skill_TypeUpdate
from app.models.user import User

router = APIRouter()

@router.get("/read/{id}", response_model=Skill_Type)
async def read_skill_type(
    id: int,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get a skill_types.
    """
    skill_type = await crud.skill_type.get_by_id(db=db, id=id)
    if not skill_type:
        raise HTTPException(status_code=404, detail="Skill type not found")
    return skill_type

@router.get("/read", response_model=List[Skill_Type])
async def read_skill_types(
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Retrieve a skill_types.
    """
    return await crud.skill_type.get_all(db=db)

@router.post("/create", response_model=Skill_Type)
async def create_skill_type(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    skill_type_in: Skill_TypeCreate
) -> Any:
    """
    Create new skill_types.
    """
    return await crud.skill_type.create(db=db, obj_in=skill_type_in)

@router.put("/update/{id}", response_model=Skill_Type)
async def update_skill_type(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int,
    skill_type_in: Skill_TypeUpdate
) -> Any:
    """
    Update a skill_types.
    """
    skill_type = await crud.skill_type.get_by_id(db=db, id=id)
    if not skill_type:
        raise HTTPException(status_code=404, detail="Skill type not found")
    skill_type = await crud.skill_type.update(db=db, db_obj=skill_type, obj_in=skill_type_in)
    return skill_type

@router.delete("/delete/{id}", response_model=Skill_Type)
async def delete_skill_type(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int
) -> Any:
    """
    Delete a skill_types.
    """
    skill_type = await crud.skill_type.get_by_id(db=db, id=id)
    if not skill_type:
        raise HTTPException(status_code=404, detail="Skill type not found")
    return await crud.skill_type.remove(db=db, id=id)
