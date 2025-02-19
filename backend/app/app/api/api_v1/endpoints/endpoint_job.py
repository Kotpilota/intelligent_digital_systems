from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, List

from app import crud
from app.api import deps
from app.schemas.job import Job, JobCreate, JobUpdate
from app.models.user import User

router = APIRouter()

@router.get("/read/{id}", response_model=Job)
async def read_job(
    id: int,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get a job.
    """
    job = await crud.job.get_by_id(db=db, id=id)
    if not job:
        raise HTTPException(status_code=404, detail="job not found")
    return job

@router.get("/read", response_model=List[Job])
async def read_jobs(
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get all jobs.
    """
    return await crud.job.get_all(db=db)

@router.post("/create", response_model=Job)
async def create_job(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    job_in: JobCreate
) -> Any:
    """
    Create a new job.
    """
    return await crud.job.create(db=db, obj_in=job_in)

@router.put("/update/{id}", response_model=Job)
async def update_job(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int,
    job_in: JobUpdate
) -> Any:
    """
    Update a job.
    """
    job = await crud.job.get_by_id(db=db, id=id)
    if not job:
        raise HTTPException(status_code=404, detail="job not found")
    job = await crud.job.update(db=db, db_obj=job, obj_in=job_in)
    return job

@router.delete("/delete/{id}", response_model=Job)
async def delete_job(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int
) -> Any:
    """
    Delete a job.
    """
    job = await crud.job.get_by_id(db=db, id=id)
    if not job:
        raise HTTPException(status_code=404, detail="job not found")
    return await crud.job.remove(db=db, id=id)
