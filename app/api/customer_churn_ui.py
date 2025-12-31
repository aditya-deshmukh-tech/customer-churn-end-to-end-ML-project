from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import logging
from app.core.config import BASE_DIR
from fastapi.templating import Jinja2Templates

router = APIRouter()

template = Jinja2Templates(directory=str(BASE_DIR / "templates"))

logger = logging.getLogger(__name__)


@router.get("/customer_churn_ui", response_class=HTMLResponse)
async def churn_ui(request: Request):
    return template.TemplateResponse("index.html", {"request" : request, "message" : "Hello fro model"})