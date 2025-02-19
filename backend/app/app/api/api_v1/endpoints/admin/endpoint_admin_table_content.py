import requests
from pathlib import Path
from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


router = APIRouter()

BASE_PATH = Path(__file__).resolve().parent.parent.parent.parent.parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

@router.get("/admin_db_tables", response_class=HTMLResponse, summary="Админка")
async def table_content_page(request: Request):
    return TEMPLATES.TemplateResponse("admin/admin_table_content.html", {"request": request})