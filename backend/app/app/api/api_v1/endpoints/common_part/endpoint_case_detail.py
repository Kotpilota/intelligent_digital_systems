import requests
from pathlib import Path
from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


router = APIRouter()

BASE_PATH = Path(__file__).resolve().parent.parent.parent.parent.parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))


@router.get("/case_detail", response_class=HTMLResponse, summary="case_detail")
async def case_detail_page(request: Request):
    return TEMPLATES.TemplateResponse(
        "common_part/pages/case_detail.html", {"request": request}
    )
