import requests
from pathlib import Path
from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


router = APIRouter()

BASE_PATH = Path(__file__).resolve().parent.parent.parent.parent.parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))


@router.get("/job_postings", response_class=HTMLResponse, summary="Вакансии")
async def job_postings_page(request: Request):
    return TEMPLATES.TemplateResponse(
        "common_part/pages/job postings.html", {"request": request}
    )
