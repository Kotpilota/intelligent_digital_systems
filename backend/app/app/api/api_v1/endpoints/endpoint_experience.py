from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, List

from app import crud
from app.api import deps
from app.schemas.experience import Experience, ExperienceCreate, ExperienceUpdate
from app.models.user import User

router = APIRouter()

@router.get("/read/{id}", response_model=Experience)
async def read_experience(
    id: int,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get a experience.
    """
    experience = await crud.experience.get_by_id(db=db, id=id)
    if not experience:
        raise HTTPException(status_code=404, detail="experience not found")
    return experience

@router.get("/read", response_model=List[Experience])
async def read_experiences(
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get all experiences.
    """
    return await crud.experience.get_all(db=db)

@router.post("/create", response_model=Experience)
async def create_experience(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    experience_in: ExperienceCreate
) -> Any:
    """
    Create a new experience.
    """
    return await crud.experience.create(db=db, obj_in=experience_in)

@router.put("/update/{id}", response_model=Experience)
async def update_experience(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int,
    experience_in: ExperienceUpdate
) -> Any:
    """
    Update a experience.
    """
    experience = await crud.experience.get_by_id(db=db, id=id)
    if not experience:
        raise HTTPException(status_code=404, detail="experience not found")
    experience = await crud.experience.update(db=db, db_obj=experience, obj_in=experience_in)
    return experience

@router.delete("/delete/{id}", response_model=Experience)
async def delete_experience(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int
) -> Any:
    """
    Delete a experience.
    """
    experience = await crud.experience.get_by_id(db=db, id=id)
    if not experience:
        raise HTTPException(status_code=404, detail="experience not found")
    return await crud.experience.remove(db=db, id=id)
