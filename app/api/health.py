from fastapi import APIRouter
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/health")
def health_check():
    logger.info("Health check called")
    return {"status": "ok"}
        