from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Optional, List

from app import crud, models
from app.api import deps
from app.models.user import User
from app.schemas.participant import Participant, ParticipantCreate, ParticipantUpdate


router = APIRouter()


@router.get('/read/{id}',  response_model=Participant)
async def read_participant(id: int,   
                           db: AsyncSession = Depends(deps.get_db),
                           current_user: User = Depends(deps.get_current_user)) -> Any:
    """
    Get a participant.
    """

    participant = await crud.participant.get_by_id(db=db, id=id)
    if not participant:
        raise HTTPException(status_code=400, detail="participant doesn't exists")
    return participant


@router.get('/read', response_model=List[Participant])
async def read_participants(db: AsyncSession = Depends(deps.get_db),
                            current_user: User = Depends(deps.get_current_user))->Any:
    """
    Retrieve category.
    """
    return await crud.participant.get_all(db)


@router.post('/create', response_model= Participant)
async def create_participant(*, db: AsyncSession = Depends(deps.get_db), 
                        participant_in: ParticipantCreate,
                        current_user: User = Depends(deps.get_current_user)  
                        ) -> Any:
    """
    Create new participant.
    """
    return await crud.participant.create(db=db, obj_in=participant_in)



@router.put('/update/{id}', response_model= Participant)
async def update_participant(*, db: AsyncSession = Depends(deps.get_db), 
                        id: int, participant_in: ParticipantUpdate,
                        current_user: User = Depends(deps.get_current_user)  
                        ) -> Any:
    """
    Update a participant.
    """
    participant = await crud.participant.get_by_id(db=db, id=id)
    if not participant:
        raise HTTPException( status_code=404, detail="participant doesn't exist",)
    participant = await crud.participant.update(db=db, db_obj=participant, obj_in=participant_in)
    return participant


@router.delete('/delete/{id}', response_model= Participant)
async def delete_participant(*, db: AsyncSession = Depends(deps.get_db), 
                        id: int,
                        current_user: User = Depends(deps.get_current_user)  
                        ) -> Any:
    """
    Delete an participant.
    """
    participant = await crud.participant.get_by_id(db=db, id=id)
    if not participant:
        raise HTTPException(status_code=404, detail="participant doesn't exist")

    return await crud.participant.remove(db=db, id=id)