import requests
from pathlib import Path
from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


router = APIRouter()

BASE_PATH = Path(__file__).resolve().parent.parent.parent.parent.parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

@router.get("/chat_page_exit", response_class=HTMLResponse, summary="Чат")
async def chat_page_exit(request: Request):
    return TEMPLATES.TemplateResponse("personal_account/chat_page_exit.html", {"request": request})