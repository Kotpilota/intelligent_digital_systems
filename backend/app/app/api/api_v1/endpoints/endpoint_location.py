from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, List

from app import crud
from app.api import deps
from app.schemas.location import Location, LocationCreate, LocationUpdate
from app.models.user import User

router = APIRouter()

@router.get("/read/{id}", response_model=Location)
async def read_location(
    id: int,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get a locations.
    """
    location = await crud.location.get_by_id(db=db, id=id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location

@router.get("/read", response_model=List[Location])
async def read_locations(
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Retrieve locations.
    """
    return await crud.location.get_all(db=db)

@router.post("/create", response_model=Location)
async def create_location(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    location_in: LocationCreate
) -> Any:
    """
    Create new locations.
    """
    return await crud.location.create(db=db, obj_in=location_in)

@router.put("/update/{id}", response_model=Location)
async def update_location(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int,
    location_in: LocationUpdate
) -> Any:
    """
    Update a locations.
    """
    location = await crud.location.get_by_id(db=db, id=id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    location = await crud.location.update(db=db, db_obj=location, obj_in=location_in)
    return location

@router.delete("/delete/{id}", response_model=Location)
async def delete_location(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int
) -> Any:
    """
    Delete a locations.
    """
    location = await crud.location.get_by_id(db=db, id=id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return await crud.location.remove(db=db, id=id)
