import math
import random
from typing import Any

import requests
from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
# from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID, uuid4

import app.schemas.user
from app import crud
from app import schemas
from app.api import deps
from app.core.auth import (authenticate, create_access_token, create_activation_token, _decode_token)
from app.core.security import get_password_hash
from app.core.execptions.exception import *
from app.core.config import settings
from app.models.user import User
from app.schemas.auth import AuthPhoneForm
from app.schemas import SessionData

from fastapi.responses import HTMLResponse
from pathlib import Path
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse 


router = APIRouter()

BASE_PATH = Path(__file__).resolve().parent.parent.parent.parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))



@router.post("/register", response_model=schemas.user.User, status_code=201)  # 1
async def register(
        *,
        db: AsyncSession = Depends(deps.get_db),  # 2
        userregister_in: schemas.user.UserRegister,  # 3
        request: Request
) -> Any:
    """
    Create new user without the need to be logged in.
    """

    user = await crud.user.get_one_or_none_by_filter(db=db, phone=userregister_in.phone)  # 4
    if user:
        raise UserAlreadyExistsException

    if userregister_in.password != userregister_in.password_check:
        raise PasswordMismatchException

    user_in = schemas.UserCreate(
        nickname=userregister_in.nickname,
        hashed_password=get_password_hash(userregister_in.password),
        phone=userregister_in.phone,
        activated=userregister_in.activated,
        role_id=userregister_in.role_id
    )
    created_user = await crud.user.create(
        db=db,
        obj_in=user_in
    )

    return created_user


@router.post("/login", )  # response_model=app.schemas.user.User)
# async def login(db: AsyncSession = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
async def login(*, request: Request, response: Response, db: AsyncSession = Depends(deps.get_db), form_data: AuthPhoneForm) -> Any:
    """
    Get the JWT for a user with data from OAuth2 request form body.
    """

    # user = await authenticate(phone=form_data.username, password=form_data.password, db=db)  # 2
    user = await authenticate(phone=form_data.phone, password=form_data.password, db=db)  # 2

    if not user:
        raise IncorrectPhoneOrPasswordException

    access_token = create_access_token(sub=user.id)
    response.set_cookie(key="ids_user_access_token", value=access_token, httponly=True)
    user = jsonable_encoder(user)

    data ={
            "ok": True,
            "access_token": access_token,  # 4
            "token_type": "bearer",
            "refresh_token": None,
            "message": "Авторизация успешна!",
            "user": user
        }
    
    """ 
    if user['role_id'] == 1:
        return TEMPLATES.TemplateResponse("personal_account/profile.html", {"request": request, "data": data})
    elif user['role_id'] == 2:
        return TEMPLATES.TemplateResponse("personal_account/account.html", {"request": request, "data": data})
    elif user['role_id'] in [3, 4]:
        return TEMPLATES.TemplateResponse("admin/dashboard.html", {"request": request, "data": data})
    """

    if user['role_id'] == 1:
        response = RedirectResponse(url='/profile', status_code=200)
        response.set_cookie(key="ids_user_access_token", value=access_token, httponly=True)
        response.body = data
        return response
    
    elif user['role_id'] == 2:
        response = RedirectResponse(url='/account', status_code=200)
        response.set_cookie(key="ids_user_access_token", value=access_token, httponly=True)
        response.body = data
        return response
    
    elif user['role_id'] in [3, 4]: 
        response = RedirectResponse(url='/dashboard', status_code=200)
        response.set_cookie(key="ids_user_access_token", value=access_token, httponly=True)
        response.body = data
        return response


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie(key="ids_user_access_token")
    return {'message': 'Пользователь успешно вышел из системы'}



@router.get("/me", response_model=schemas.user.User)
async def get_me(current_user: User = Depends(deps.get_current_user)):
    """
    Fetch the current logged in user.
    """
    return current_user


@router.post("/activate/{token}/{action}", response_model=schemas.user.User, status_code=201)
async def activate(*, token, action: str, db: AsyncSession = Depends(deps.get_db)):
    phone = _decode_token(token=token)
    user = await crud.user.get_by_phone(db=db, phone=phone)

    if not user:
        raise HTTPException(status_code=404, detail="user doesn't exist", )

    user_in = schemas.user.UserUpdate(**jsonable_encoder(user))
    if action == "activate":
        user_in.activated = True
    else:
        user_in.activated = False

    if isinstance(user_in, dict):
        update_data = user_in
    else:
        # update_data = user_in.dict(exclude_unset=True)
        update_data = dict(user_in)

    if update_data.get("hashed_password"):
        del update_data["hashed_password"]

    user = await crud.user.update(db=db, db_obj=user, obj_in=update_data)
    return user


@router.post("/deactivate/{token}", response_model=schemas.user.User, status_code=201)
async def deactivate(*, token, db: AsyncSession = Depends(deps.get_db)):
    phone = _decode_token(token=token)
    user = await crud.user.get_by_phone(db=db, phone=phone)

    if not user:
        raise HTTPException(status_code=404, detail="user doesn't exist", )

    user_in = schemas.user.UserUpdate(**jsonable_encoder(user))
    user_in.activated = False

    if isinstance(user_in, dict):
        update_data = user_in
    else:
        # update_data = user_in.dict(exclude_unset=True)
        update_data = dict(user_in)

    if update_data.get("hashed_password"):
        del update_data["hashed_password"]

    user = await crud.user.update(db=db, db_obj=user, obj_in=update_data)
    return user





# skipping...

@router.post("/create_session/{name}")
async def create_session(name:str, response: Response):
    session = uuid4()
    data = SessionData(username=name)

    await deps.backend.create(session, data)
    deps.cookie.attach_to_response(response, session)

    return f"created session for {name}"

@router.get("/get_session", dependencies=[Depends(deps.cookie)])
async def get_session(session_data: SessionData = Depends(deps.verifier) ):
    return session_data

@router.post("/delete_session")
async def del_session(response: Response, session_id: UUID = Depends(deps.cookie)):
    await deps.backend.delete(session_id)
    deps.cookie.delete_from_response(response)
    return "deleted session"