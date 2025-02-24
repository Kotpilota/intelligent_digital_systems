from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Optional, List

from app import crud, models
from app.api import deps
from app.models.user import User
from app.schemas.assigned_task import Assigned_Task, Assigned_TaskCreate, Assigned_TaskUpdate


router = APIRouter()


@router.get('/read/{id}',  response_model=Assigned_Task)
async def read_assigned_task(id: int,   
                             db: AsyncSession = Depends(deps.get_db),
                             current_user: User = Depends(deps.get_current_user)) -> Any:
    """
    Get a assigned_task.
    """

    assigned_task = await crud.assigned_task.get_by_id(db=db, id=id)
    if not assigned_task:
        raise HTTPException(status_code=400, detail="assigned_task doesn't exists")
    return assigned_task


@router.get('/read', response_model=List[Assigned_Task])
async def read_assigned_tasks(db: AsyncSession = Depends(deps.get_db),
                              current_user: User = Depends(deps.get_current_user))->Any:
    """
    Retrieve category.
    """
    return await crud.assigned_task.get_all(db)


@router.post('/create', response_model= Assigned_Task)
async def create_assigned_task(*, db: AsyncSession = Depends(deps.get_db), 
                        assigned_task_in: Assigned_TaskCreate,
                        current_user: User = Depends(deps.get_current_user)  
                        ) -> Any:
    """
    Create new assigned_task.
    """
    return await crud.assigned_task.create(db=db, obj_in=assigned_task_in)



@router.put('/update/{id}', response_model= Assigned_Task)
async def update_assigned_task(*, db: AsyncSession = Depends(deps.get_db), 
                        id: int, assigned_task_in: Assigned_TaskUpdate,
                        current_user: User = Depends(deps.get_current_user)  
                        ) -> Any:
    """
    Update a assigned_task.
    """
    assigned_task = await crud.assigned_task.get_by_id(db=db, id=id)
    if not assigned_task:
        raise HTTPException( status_code=404, detail="assigned_task doesn't exist",)
    updated_assigned_task = await crud.assigned_task.update(db=db, db_obj=assigned_task, obj_in=assigned_task_in)
    return updated_assigned_task


@router.delete('/delete/{id}', response_model= Assigned_Task)
async def delete_assigned_task(*, db: AsyncSession = Depends(deps.get_db), 
                        id: int,
                        current_user: User = Depends(deps.get_current_user)  
                        ) -> Any:
    """
    Delete an assigned_task.
    """
    assigned_task = await crud.assigned_task.get_by_id(db=db, id=id)
    if not assigned_task:
        raise HTTPException(status_code=404, detail="assigned_task doesn't exist")

    return await crud.assigned_task.remove(db=db, id=id)