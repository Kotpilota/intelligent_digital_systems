from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Optional, List

from app import crud, models
from app.api import deps
from app.models.user import User
from app.schemas.project import Project, ProjectCreate, ProjectUpdate


router = APIRouter()


@router.get('/read/{id}',  response_model=Project)
async def read_project(id: int,   
                       db: AsyncSession = Depends(deps.get_db),
                       current_user: User = Depends(deps.get_current_user)) -> Any:
    """
    Get a project.
    """

    project = await crud.project.get_by_id(db=db, id=id)
    if not project:
        raise HTTPException(status_code=400, detail="project doesn't exists")
    return project


@router.get('/read', response_model=List[Project])
async def read_projects(db: AsyncSession = Depends(deps.get_db),
                        current_user: User = Depends(deps.get_current_user))->Any:
    """
    Retrieve category.
    """
    return await crud.project.get_all(db)


@router.post('/create', response_model= Project)
async def create_project(*, db: AsyncSession = Depends(deps.get_db), 
                        project_in: ProjectCreate,
                        current_user: User = Depends(deps.get_current_user)  
                        ) -> Any:
    """
    Create new project.
    """
    return await crud.project.create(db=db, obj_in=project_in)



@router.put('/update/{id}', response_model= Project)
async def update_project(*, db: AsyncSession = Depends(deps.get_db), 
                        id: int, project_in: ProjectUpdate,
                        current_user: User = Depends(deps.get_current_user)  
                        ) -> Any:
    """
    Update a project.
    """
    project = await crud.project.get_by_id(db=db, id=id)
    if not project:
        raise HTTPException( status_code=404, detail="project doesn't exist",)
    project = await crud.project.update(db=db, db_obj=project, obj_in=project_in)
    return project


@router.delete('/delete/{id}', response_model= Project)
async def delete_project(*, db: AsyncSession = Depends(deps.get_db), 
                        id: int,
                        current_user: User = Depends(deps.get_current_user)  
                        ) -> Any:
    """
    Delete an project.
    """
    project = await crud.project.get_by_id(db=db, id=id)
    if not project:
        raise HTTPException(status_code=404, detail="project doesn't exist")

    return await crud.project.remove(db=db, id=id)