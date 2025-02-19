from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Optional, List

from app import crud, models
from app.api import deps
from app.models.user import User
from app.schemas.project_document import Project_Document, Project_DocumentCreate, Project_DocumentUpdate


router = APIRouter()


@router.get('/read/{id}',  response_model=Project_Document)
async def read_project_document(id: int,   
                                db: AsyncSession = Depends(deps.get_db),
                                current_user: User = Depends(deps.get_current_user)) -> Any:
    """
    Get a project_document.
    """

    project_document = await crud.project_document.get_by_id(db=db, id=id)
    if not project_document:
        raise HTTPException(status_code=400, detail="project_document doesn't exists")
    return project_document


@router.get('/read', response_model=List[Project_Document])
async def read_project_documents(db: AsyncSession = Depends(deps.get_db),
                                 current_user: User = Depends(deps.get_current_user))->Any:
    """
    Retrieve category.
    """
    return await crud.project_document.get_all(db)


@router.post('/create', response_model= Project_Document)
async def create_project_document(*, db: AsyncSession = Depends(deps.get_db), 
                        project_document_in: Project_DocumentCreate,
                        current_user: User = Depends(deps.get_current_user)  
                        ) -> Any:
    """
    Create new project_document.
    """
    return await crud.project_document.create(db=db, obj_in=project_document_in)



@router.put('/update/{id}', response_model= Project_Document)
async def update_project_document(*, db: AsyncSession = Depends(deps.get_db), 
                        id: int, project_document_in: Project_DocumentUpdate,
                        current_user: User = Depends(deps.get_current_user)  
                        ) -> Any:
    """
    Update a project_document.
    """
    project_document = await crud.project_document.get_by_id(db=db, id=id)
    if not project_document:
        raise HTTPException( status_code=404, detail="project_document doesn't exist",)
    project_document = await crud.project_document.update(db=db, db_obj=project_document, obj_in=project_document_in)
    return project_document


@router.delete('/delete/{id}', response_model= Project_Document)
async def delete_project_document(*, db: AsyncSession = Depends(deps.get_db), 
                        id: int,
                        current_user: User = Depends(deps.get_current_user)  
                        ) -> Any:
    """
    Delete an project_document.
    """
    project_document = await crud.project_document.get_by_id(db=db, id=id)
    if not project_document:
        raise HTTPException(status_code=404, detail="project_document doesn't exist")

    return await crud.project_document.remove(db=db, id=id)