from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Optional, List

from app import crud, models
from app.api import deps
from app.models.user import User
from app.schemas.project_document_type import Project_Document_Type, Project_Document_TypeCreate, Project_Document_TypeUpdate


router = APIRouter()


@router.get('/read/{id}',  response_model=Project_Document_Type)
async def read_project_document_type(id: int,   
                                     db: AsyncSession = Depends(deps.get_db),
                                     current_user: User = Depends(deps.get_current_user)) -> Any:
    """
    Get a project_document_type.
    """

    project_document_type = await crud.project_document_type.get_by_id(db=db, id=id)
    if not project_document_type:
        raise HTTPException(status_code=400, detail="project_document_type doesn't exists")
    return project_document_type


@router.get('/read', response_model=List[Project_Document_Type])
async def read_project_document_types(db: AsyncSession = Depends(deps.get_db),
                                      current_user: User = Depends(deps.get_current_user))->Any:
    """
    Retrieve category.
    """
    return await crud.project_document_type.get_all(db)


@router.post('/create', response_model= Project_Document_Type)
async def create_project_document_type(*, db: AsyncSession = Depends(deps.get_db), 
                        project_document_type_in: Project_Document_TypeCreate,
                        current_user: User = Depends(deps.get_current_user)  
                        ) -> Any:
    """
    Create new project_document_type.
    """
    return await crud.project_document_type.create(db=db, obj_in=project_document_type_in)



@router.put('/update/{id}', response_model= Project_Document_Type)
async def update_project_document_type(*, db: AsyncSession = Depends(deps.get_db), 
                        id: int, project_document_type_in: Project_Document_TypeUpdate,
                        current_user: User = Depends(deps.get_current_user)  
                        ) -> Any:
    """
    Update a project_document_type.
    """
    project_document_type = await crud.project_document_type.get_by_id(db=db, id=id)
    if not project_document_type:
        raise HTTPException( status_code=404, detail="project_document_type doesn't exist",)
    project_document_type = await crud.project_document_type.update(db=db, db_obj=project_document_type, obj_in=project_document_type_in)
    return project_document_type


@router.delete('/delete/{id}', response_model= Project_Document_Type)
async def delete_project_document_type(*, db: AsyncSession = Depends(deps.get_db), 
                        id: int,
                        current_user: User = Depends(deps.get_current_user)  
                        ) -> Any:
    """
    Delete an project_document_type.
    """
    project_document_type = await crud.project_document_type.get_by_id(db=db, id=id)
    if not project_document_type:
        raise HTTPException(status_code=404, detail="project_document_type doesn't exist")

    return await crud.project_document_type.remove(db=db, id=id)