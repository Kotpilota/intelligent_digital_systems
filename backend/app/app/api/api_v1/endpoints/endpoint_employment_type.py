from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, List

from app import crud
from app.api import deps
from app.schemas.employment_type import Employment_Type, Employment_TypeCreate, Employment_TypeUpdate
from app.models.user import User

router = APIRouter()

@router.get("/read/{id}", response_model=Employment_Type)
async def read_employment_type(
    id: int,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get an emloyment_type.
    """
    emp_type = await crud.employment_type.get_by_id(db=db, id=id)
    if not emp_type:
        raise HTTPException(status_code=404, detail="Employment type not found")
    return emp_type

@router.get("/read", response_model=List[Employment_Type])
async def read_employment_types(
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Retrieve emloyment_type.
    """
    return await crud.employment_type.get_all(db=db)

@router.post("/create", response_model=Employment_Type)
async def create_employment_type(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    emp_type_in: Employment_TypeCreate
) -> Any:
    """
    Create new emloyment_type.
    """
    return await crud.employment_type.create(db=db, obj_in=emp_type_in)

@router.put("/update/{id}", response_model=Employment_Type)
async def update_employment_type(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int,
    emp_type_in: Employment_TypeUpdate
) -> Any:
    """
    Update an emloyment_type.
    """
    emp_type = await crud.employment_type.get_by_id(db=db, id=id)
    if not emp_type:
        raise HTTPException(status_code=404, detail="Employment type not found")
    emp_type = await crud.employment_type.update(db=db, db_obj=emp_type, obj_in=emp_type_in)
    return emp_type

@router.delete("/delete/{id}", response_model=Employment_Type)
async def delete_employment_type(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int
) -> Any:
    """
    Delete an emloyment_type.
    """
    emp_type = await crud.employment_type.get_by_id(db=db, id=id)
    if not emp_type:
        raise HTTPException(status_code=404, detail="Employment type not found")
    return await crud.employment_type.remove(db=db, id=id)
