from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, List

from app import crud
from app.api import deps
from app.schemas.message import Message, MessageCreate, MessageUpdate
from app.models.user import User

router = APIRouter()

@router.get("/read/{id}", response_model=Message)
async def read_message(
    id: int,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get a message.
    """
    message = await crud.message.get_by_id(db=db, id=id)
    if not message:
        raise HTTPException(status_code=404, detail="message not found")
    return message

@router.get("/read", response_model=List[Message])
async def read_messages(
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get all messages.
    """
    return await crud.message.get_all(db=db)

@router.post("/create", response_model=Message)
async def create_message(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    message_in: MessageCreate
) -> Any:
    """
    Create a new message.
    """
    return await crud.message.create(db=db, obj_in=message_in)

@router.put("/update/{id}", response_model=Message)
async def update_message(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int,
    message_in: MessageUpdate
) -> Any:
    """
    Update a message.
    """
    message = await crud.message.get_by_id(db=db, id=id)
    if not message:
        raise HTTPException(status_code=404, detail="message not found")
    message = await crud.message.update(db=db, db_obj=message, obj_in=message_in)
    return message

@router.delete("/delete/{id}", response_model=Message)
async def delete_message(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int
) -> Any:
    """
    Delete a message.
    """
    message = await crud.message.get_by_id(db=db, id=id)
    if not message:
        raise HTTPException(status_code=404, detail="message not found")
    return await crud.message.remove(db=db, id=id)
