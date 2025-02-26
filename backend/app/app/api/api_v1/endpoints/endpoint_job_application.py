from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, List

from app import crud
from app.api import deps
from app.schemas.job_application import Job_Application, Job_ApplicationCreate, Job_ApplicationUpdate
from app.models.user import User

router = APIRouter()

@router.get("/read/{id}", response_model=Job_Application)
async def read_job_application(
    id: int,
    db: AsyncSession = Depends(deps.get_db)
) -> Any:
    """
    Get a job_application.
    """
    job_application = await crud.job_application.get_by_id(db=db, id=id)
    if not job_application:
        raise HTTPException(status_code=404, detail="job_application not found")
    return job_application

@router.get("/read", response_model=List[Job_Application])
async def read_job_applications(
    db: AsyncSession = Depends(deps.get_db)
) -> Any:
    """
    Get all job_applications.
    """
    return await crud.job_application.get_all(db=db)

@router.post("/create", response_model=Job_Application)
async def create_job_application(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    job_application_in: Job_ApplicationCreate
) -> Any:
    """
    Create a new job_application.
    """
    return await crud.job_application.create(db=db, obj_in=job_application_in)

@router.put("/update/{id}", response_model=Job_Application)
async def update_job_application(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int,
    job_application_in: Job_ApplicationUpdate
) -> Any:
    """
    Update a job_application.
    """
    job_application = await crud.job_application.get_by_id(db=db, id=id)
    if not job_application:
        raise HTTPException(status_code=404, detail="job_application not found")
    job_application = await crud.job_application.update(db=db, db_obj=job_application, obj_in=job_application_in)
    return job_application

@router.delete("/delete/{id}", response_model=Job_Application)
async def delete_job_application(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int
) -> Any:
    """
    Delete a job_application.
    """
    job_application = await crud.job_application.get_by_id(db=db, id=id)
    if not job_application:
        raise HTTPException(status_code=404, detail="job_application not found")
    return await crud.job_application.remove(db=db, id=id)
