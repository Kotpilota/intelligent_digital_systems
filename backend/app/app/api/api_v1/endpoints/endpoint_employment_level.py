from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, List

from app import crud
from app.api import deps
from app.schemas.employment_level import (
    Employment_Level,
    Employment_LevelCreate,
    Employment_LevelUpdate,
)
from app.models.user import User

router = APIRouter()

@router.get("/read/{id}", response_model=Employment_Level)
async def read_employment_level(
    id: int,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    """
    Get an employment_level.
    """
    emp_level = await crud.employment_level.get_by_id(db=db, id=id)
    if not emp_level:
        raise HTTPException(status_code=404, detail="Employment level not found")
    return emp_level

@router.get("/read", response_model=List[Employment_Level])
async def read_employment_levels(
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    """
    Retrieve employment_level.
    """
    return await crud.employment_level.get_all(db=db)

@router.post("/create", response_model=Employment_Level)
async def create_employment_level(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    emp_level_in: Employment_LevelCreate
) -> Any:
    """
    Create new employment_level.
    """
    return await crud.employment_level.create(db=db, obj_in=emp_level_in)

@router.put("/update/{id}", response_model=Employment_Level)
async def update_employment_level(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int,
    emp_level_in: Employment_LevelUpdate
) -> Any:
    """
    Update an employment_level.
    """
    emp_level = await crud.employment_level.get_by_id(db=db, id=id)
    if not emp_level:
        raise HTTPException(status_code=404, detail="Employment level not found")
    emp_level = await crud.employment_level.update(db=db, db_obj=emp_level, obj_in=emp_level_in)
    return emp_level

@router.delete("/delete/{id}", response_model=Employment_Level)
async def delete_employment_level(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int
) -> Any:
    """
    Delete an employment_level.
    """
    emp_level = await crud.employment_level.get_by_id(db=db, id=id)
    if not emp_level:
        raise HTTPException(status_code=404, detail="Employment level not found")
    return await crud.employment_level.remove(db=db, id=id)
