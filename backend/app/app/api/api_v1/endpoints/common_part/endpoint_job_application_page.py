import requests
from pathlib import Path
from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.api import deps
from app import crud

router = APIRouter()

BASE_PATH = Path(__file__).resolve().parent.parent.parent.parent.parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))


@router.get(
    "/job_application_page/{id}",
    response_class=HTMLResponse,
    summary="Заявление о приеме на работу",
)
async def job_application_page(
        id: int,
        request: Request,
        db: AsyncSession = Depends(deps.get_db)
):
    job = await crud.job.get_by_id(db=db, id=id)

    if not job:
        raise HTTPException(status_code=404, detail="Вакансия не найдена")

    return TEMPLATES.TemplateResponse(
        "common_part/pages/job_application.html",
        {"request": request, "job": job}
    )