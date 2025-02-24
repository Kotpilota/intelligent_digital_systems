from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, List

from app import crud
from app.api import deps
from app.schemas.has_skill import Has_Skill, Has_SkillCreate, Has_SkillUpdate
from app.models.user import User

router = APIRouter()

@router.get("/read/{id}", response_model=Has_Skill)
async def read_has_skill(
    id: int,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get a has_skils.
    """
    has_skill = await crud.has_skill.get_by_id(db=db, id=id)
    if not has_skill:
        raise HTTPException(status_code=404, detail="HasSkill record not found")
    return has_skill

@router.get("/read", response_model=List[Has_Skill])
async def read_has_skils(
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Retrieve a has_skils
    """
    return await crud.has_skill.get_all(db=db)

@router.post("/create", response_model=Has_Skill)
async def create_has_skill(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    has_skill_in: Has_SkillCreate
) -> Any:
    """
    Create new has_skils
    """
    return await crud.has_skill.create(db=db, obj_in=has_skill_in)

@router.put("/update/{id}", response_model=Has_Skill)
async def update_has_skill(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int,
    has_skill_in: Has_SkillUpdate
) -> Any:
    """
    Update a has_skils
    """
    has_skill = await crud.has_skill.get_by_id(db=db, id=id)
    if not has_skill:
        raise HTTPException(status_code=404, detail="HasSkill record not found")
    has_skill = await crud.has_skill.update(db=db, db_obj=has_skill, obj_in=has_skill_in)
    return has_skill

@router.delete("/delete/{id}", response_model=Has_Skill)
async def delete_has_skill(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int
) -> Any:
    """
    Delete a has_skils
    """
    has_skill = await crud.has_skill.get_by_id(db=db, id=id)
    if not has_skill:
        raise HTTPException(status_code=404, detail="HasSkill record not found")
    return await crud.has_skill.remove(db=db, id=id)
