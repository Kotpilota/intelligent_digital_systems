import time
from pathlib import Path

from fastapi import FastAPI, APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from app import crud
from app.api import deps

# Here importing your custom api routers
# in your project you have to complete this importing
from app.api.api_v1.api import api_router

from app.core.config import settings

from fastapi import HTTPException, Request, status
from fastapi.responses import RedirectResponse, JSONResponse
from urllib.parse import quote


BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

app = FastAPI(title="Intelligent Digital Systems Web Site")

app.mount("/static", StaticFiles(directory=str(BASE_PATH / "static")), name="static")

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        # allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_origins=["*"],
        allow_origin_regex=settings.BACKEND_CORS_ORIGIN_REGEX,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == status.HTTP_401_UNAUTHORIZED:
        # URL-encode the error detail to handle special characters
        error_detail = quote(exc.detail)
        # error_url = f"/auth/unauthorized?detail={error_detail}"
        error_url = f"/auth/unauthorized"
        return RedirectResponse(url=error_url, status_code=303)  # 303 for redirect
    # Return default JSON for other errors
    return JSONResponse( status_code=exc.status_code, content={"detail": exc.detail},)


# Here including custom routers in app
# in your project you have to complete app.include_router( , prefix=)
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn


    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="debug")

