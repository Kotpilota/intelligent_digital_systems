from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Optional, List

from app import crud, models
from app.api import deps
from app.schemas.task import Task, TaskCreate, TaskUpdate
from app.models.user import User


router = APIRouter()


@router.get('/read/{id}',  response_model=Task)
async def read_task(id: int,   
                    db: AsyncSession = Depends(deps.get_db),
                    current_user: User = Depends(deps.get_current_user)) -> Any:
    """
    Get a task.
    """

    task = await crud.task.get_by_id(db=db, id=id)
    if not task:
        raise HTTPException(status_code=400, detail="task doesn't exists")
    return task


@router.get('/read', response_model=List[Task])
async def read_tasks(db: AsyncSession = Depends(deps.get_db),
                     current_user: User = Depends(deps.get_current_user)) -> Any:
    """
    Retrieve category.
    """
    return await crud.task.get_all(db)


@router.post('/create', response_model= Task)
async def create_task(*, db: AsyncSession = Depends(deps.get_db), 
                        task_in: TaskCreate,
                        current_user: User = Depends(deps.get_current_user)  
                        ) -> Any:
    """
    Create new task.
    """
    return await crud.task.create(db=db, obj_in=task_in)



@router.put('/update/{id}', response_model= Task)
async def update_task(*, db: AsyncSession = Depends(deps.get_db), 
                        id: int, task_in: TaskUpdate,
                        current_user: User = Depends(deps.get_current_user)  
                        ) -> Any:
    """
    Update a task.
    """
    task = await crud.task.get_by_id(db=db, id=id)
    if not task:
        raise HTTPException( status_code=404, detail="task doesn't exist",)
    task = await crud.task.update(db=db, db_obj=task, obj_in=task_in)
    return task


@router.delete('/delete/{id}', response_model= Task)
async def delete_task(*, db: AsyncSession = Depends(deps.get_db), 
                        id: int,
                        current_user: User = Depends(deps.get_current_user)  
                        ) -> Any:
    """
    Delete an task.
    """
    task = await crud.task.get_by_id(db=db, id=id)
    if not task:
        raise HTTPException(status_code=404, detail="task doesn't exist")

    return await crud.task.remove(db=db, id=id)