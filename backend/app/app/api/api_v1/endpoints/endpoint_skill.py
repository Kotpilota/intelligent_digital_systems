from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, List

from app import crud
from app.api import deps
from app.schemas.skill import Skill, SkillCreate, SkillUpdate
from app.models.user import User

router = APIRouter()

@router.get("/read/{id}", response_model=Skill)
async def read_skill(
    id: int,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get a skill.
    """
    skill = await crud.skill.get_by_id(db=db, id=id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill

@router.get("/read", response_model=List[Skill])
async def read_skills(
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Retrieve a skills
    """
    return await crud.skill.get_all(db=db)

@router.post("/create", response_model=Skill)
async def create_skill(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    skill_in: SkillCreate
) -> Any:
    """
    Create new skill.
    """
    return await crud.skill.create(db=db, obj_in=skill_in)

@router.put("/update/{id}", response_model=Skill)
async def update_skill(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int,
    skill_in: SkillUpdate
) -> Any:
    """
    Update a skill.
    """
    skill = await crud.skill.get_by_id(db=db, id=id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    skill = await crud.skill.update(db=db, db_obj=skill, obj_in=skill_in)
    return skill

@router.delete("/delete/{id}", response_model=Skill)
async def delete_skill(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int
) -> Any:
    """
    Delete a skill
    """
    skill = await crud.skill.get_by_id(db=db, id=id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return await crud.skill.remove(db=db, id=id)
