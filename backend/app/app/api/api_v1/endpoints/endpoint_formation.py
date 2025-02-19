from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, List

from app import crud
from app.api import deps
from app.schemas.formation import Formation, FormationCreate, FormationUpdate
from app.models.user import User

router = APIRouter()

@router.get("/read/{id}", response_model=Formation)
async def read_formation(
    id: int,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get a formation.
    """
    formation = await crud.formation.get_by_id(db=db, id=id)
    if not formation:
        raise HTTPException(status_code=404, detail="Formation not found")
    return formation

@router.get("/read", response_model=List[Formation])
async def read_formations(
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get all formations.
    """
    return await crud.formation.get_all(db=db)

@router.post("/create", response_model=Formation)
async def create_formation(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    formation_in: FormationCreate
) -> Any:
    """
    Create a new formation.
    """
    return await crud.formation.create(db=db, obj_in=formation_in)

@router.put("/update/{id}", response_model=Formation)
async def update_formation(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int,
    formation_in: FormationUpdate
) -> Any:
    """
    Update a formation.
    """
    formation = await crud.formation.get_by_id(db=db, id=id)
    if not formation:
        raise HTTPException(status_code=404, detail="formation not found")
    formation = await crud.formation.update(db=db, db_obj=formation, obj_in=formation_in)
    return formation

@router.delete("/delete/{id}", response_model=Formation)
async def delete_formation(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int
) -> Any:
    """
    Delete a formation.
    """
    formation = await crud.formation.get_by_id(db=db, id=id)
    if not formation:
        raise HTTPException(status_code=404, detail="formation not found")
    return await crud.formation.remove(db=db, id=id)
