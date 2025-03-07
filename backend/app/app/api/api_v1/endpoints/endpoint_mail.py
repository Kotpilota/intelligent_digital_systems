from fastapi import APIRouter, Depends, HTTPException # Query
# from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, List # Optional
from app import crud, models
from app.api import deps
from app.models.mail import Mail
from app.schemas.mail import Mail, MailCreate, MailUpdate
from app.models.user import User


router = APIRouter()


@router.get('/read', response_model=List[Mail])
async def read_mails(db: AsyncSession = Depends(deps.get_db),
                     current_user: models.User = Depends(deps.get_current_user)) -> Any:
    return await crud.mail.get_all(db)


@router.get('/read_mail/{id}',  response_model=Mail)
async def read_mail(id: int,   db: AsyncSession = Depends(deps.get_db),
                    current_user: User = Depends(deps.get_current_user)) -> Any:
    mail = await crud.mail.get_by_id(db=db, id=id)
    if mail is None:
        raise HTTPException(status_code=400, detail="mail doesn't exists")
    return mail


@router.post('/create_mail', response_model=MailCreate)
async def create_mail(*, db: AsyncSession = Depends(deps.get_db), 
                      current_user: User = Depends(deps.get_current_user), 
                      mail_in: MailCreate) -> Any:
    return await crud.mail.create(db=db, obj_in=mail_in)


@router.delete('/delete_mail/{id}', response_model=Mail)
async def delete_mail(*, db: AsyncSession = Depends(deps.get_db), 
                      current_user: User = Depends(deps.get_current_user), 
                      id: int) -> Any:
    mail = await crud.mail.get_by_id(db=db, id=id)
    if mail is None:
        raise HTTPException(status_code=404, detail="mail doesn't exist")
    return await crud.mail.remove(db=db, id=id)
