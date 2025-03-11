import requests
from pathlib import Path
from fastapi import APIRouter, Depends, HTTPException, Request, Response , WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import HTMLResponse
from app.api import deps
from app.models.user import User
from app.schemas.message import Message, MessageCreate, MessageUpdate
from app import crud, models
import asyncio
from typing import List, Dict

router = APIRouter(prefix='/chat', tags=['Chat'])

BASE_PATH = Path(__file__).resolve().parent.parent.parent.parent.parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))


# Страница чата
@router.get("/", response_class=HTMLResponse, summary="Чат")
async def get_chat_page(request: Request,
                        db: AsyncSession = Depends(deps.get_db),
                       current_user: User = Depends(deps.get_current_user)):
    users_all = await crud.user.get_all(db)

    return TEMPLATES.TemplateResponse("personal_account/chat_page_exit.html", 
                                      {"request": request, 'user':current_user, 'users_all': users_all})


# **************************************** 11/03/2025



@router.get("/messages/{user_id}", response_model=List[MessageRead])
async def get_messages(user_id: int, 
                       db: AsyncSession = Depends(deps.get_db), 
                       current_user: User = Depends(deps.get_current_user)
                       ):
    
    return await crud.message.get_all_by_filter() MessagesDAO.get_messages_between_users(user_id_1=user_id, user_id_2=current_user.id) or []





@router.post("/messages", response_model=MessageCreate)
async def send_message(message: MessageCreate, 
                       db: AsyncSession = Depends(deps.get_db), 
                       current_user: User = Depends(deps.get_current_user)
                       ):
    
    # Добавляем новое сообщение в базу данных
    await MessagesDAO.add(
        sender_id=current_user.id,
        content=message.content,
        recipient_id=message.recipient_id
    )
    # Подготавливаем данные для отправки сообщения
    message_data = {
        'sender_id': current_user.id,
        'recipient_id': message.recipient_id,
        'content': message.content,
    }
    # Уведомляем получателя и отправителя через WebSocket
    await notify_user(message.recipient_id, message_data)
    await notify_user(current_user.id, message_data)

    # Возвращаем подтверждение сохранения сообщения
    return {'recipient_id': message.recipient_id, 'content': message.content, 'status': 'ok', 'msg': 'Message saved!'}



# Активные WebSocket-подключения: {user_id: websocket}
active_connections: Dict[int, WebSocket] = {}


# Функция для отправки сообщения пользователю, если он подключен
async def notify_user(user_id: int, message: dict):
    """Отправить сообщение пользователю, если он подключен."""
    if user_id in active_connections:
        websocket = active_connections[user_id]
        # Отправляем сообщение в формате JSON
        await websocket.send_json(message)


# WebSocket эндпоинт для соединений
@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    # Принимаем WebSocket-соединение
    await websocket.accept()
    # Сохраняем активное соединение для пользователя
    active_connections[user_id] = websocket
    try:
        while True:
            # Просто поддерживаем соединение активным (1 секунда паузы)
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        # Удаляем пользователя из активных соединений при отключении
        active_connections.pop(user_id, None)