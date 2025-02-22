import requests
from pathlib import Path
from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.api import deps
from app.models.user import User


router = APIRouter()

BASE_PATH = Path(__file__).resolve().parent.parent.parent.parent.parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

@router.get("/profile", response_class=HTMLResponse, summary="Профиль")
async def profile_page(request: Request,
                       current_user: User = Depends(deps.get_current_user)
                       ):
    return TEMPLATES.TemplateResponse("personal_account/profile.html", {"request": request, "current_user": current_user})