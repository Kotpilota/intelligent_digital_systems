from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Optional, List

from app import crud, models
from app.api import deps
from app.schemas.role import Role, RoleCreate, RoleUpdate
from app.models.user import User

router = APIRouter()


@router.get('/read/{id}', response_model=Role)
async def read_role(id: int,
                         db: AsyncSession = Depends(deps.get_db),
                         current_user: User = Depends(deps.get_current_user)) -> Any:
    """
    Get a role.
    """

    role = await crud.role.get_by_id(db=db, id=id)
    if not role:
        raise HTTPException(status_code=400, detail="role doesn't exist")
    return role


@router.get('/read', response_model=List[Role])
async def read_roles(db: AsyncSession = Depends(deps.get_db),
                          current_user: User = Depends(deps.get_current_user)
                          ) -> Any:
    """
    Retrieve role.
    """
    return await crud.role.get_all(db)


@router.post('/create', response_model=Role)
async def create_role(*, db: AsyncSession = Depends(deps.get_db),
                           current_user: User = Depends(deps.get_current_user),
                           role_in: RoleCreate,
                           ) -> Any:
    """
    Create new role.
    """
    return await crud.role.create(db=db, obj_in=role_in)


@router.put('/update/{id}', response_model=Role)
async def update_role(*, db: AsyncSession = Depends(deps.get_db),
                           current_user: User = Depends(deps.get_current_user),
                           id: int, role_in: RoleUpdate,
                           ) -> Any:
    """
    Update a role.
    """
    role = await crud.role.get_by_id(db=db, id=id)
    if not role:
        raise HTTPException(status_code=404, detail="role doesn't exists", )
    role = await crud.role.update(db=db, db_obj=role, obj_in=role_in)
    return role


@router.delete('/delete/{id}', response_model=Role)
async def delete_role(*, db: AsyncSession = Depends(deps.get_db),
                           current_user: User = Depends(deps.get_current_user),
                           id: int,
                           ) -> Any:
    """
    Delete a role.
    """
    role = await crud.role.get_by_id(db=db, id=id)
    if not role:
        raise HTTPException(status_code=404, detail="role doesn't exists")

    return await crud.role.remove(db=db, id=id)
