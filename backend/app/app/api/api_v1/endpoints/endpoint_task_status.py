from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Optional, List

from app import crud, models
from app.api import deps
from app.schemas.task_status import Task_Status, Task_StatusCreate, Task_StatusUpdate
from app.models.user import User


router = APIRouter()


@router.get('/read/{id}',  response_model=Task_Status)
async def read_task_status(id: int,   
                           db: AsyncSession = Depends(deps.get_db),
                           current_user: User = Depends(deps.get_current_user)) -> Any:
    """
    Get a task_status.
    """

    task_status = await crud.task_status.get_by_id(db=db, id=id)
    if not task_status:
        raise HTTPException(status_code=400, detail="task_status doesn't exists")
    return task_status


@router.get('/read', response_model=List[Task_Status])
async def read_task_statuses(db: AsyncSession = Depends(deps.get_db),
                             current_user: User = Depends(deps.get_current_user))->Any:
    """
    Retrieve category.
    """
    return await crud.task_status.get_all(db)


@router.post('/create', response_model= Task_Status)
async def create_task_status(*, db: AsyncSession = Depends(deps.get_db), 
                        task_status_in: Task_StatusCreate,
                        current_user: User = Depends(deps.get_current_user)  
                        ) -> Any:
    """
    Create new task_status.
    """
    return await crud.task_status.create(db=db, obj_in=task_status_in)



@router.put('/update/{id}', response_model= Task_Status)
async def update_task_status(*, db: AsyncSession = Depends(deps.get_db), 
                        id: int, task_status_in: Task_StatusUpdate,
                        current_user: User = Depends(deps.get_current_user)  
                        ) -> Any:
    """
    Update a task_status.
    """
    task_status = await crud.task_status.get_by_id(db=db, id=id)
    if not task_status:
        raise HTTPException( status_code=404, detail="task_status doesn't exist",)
    task_status = await crud.task_status.update(db=db, db_obj=task_status, obj_in=task_status_in)
    return task_status


@router.delete('/delete/{id}', response_model= Task_Status)
async def delete_task_status(*, db: AsyncSession = Depends(deps.get_db), 
                        id: int,
                        current_user: User = Depends(deps.get_current_user)  
                        ) -> Any:
    """
    Delete an task_status.
    """
    task_status = await crud.task_status.get_by_id(db=db, id=id)
    if not task_status:
        raise HTTPException(status_code=404, detail="task_status doesn't exist")

    return await crud.task_status.remove(db=db, id=id)