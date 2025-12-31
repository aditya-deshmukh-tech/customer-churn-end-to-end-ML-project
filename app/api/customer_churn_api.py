from fastapi import APIRouter, HTTPException
from app.models.model_objs import Customer
import logging
from app.services.customer_churn_service import predict_customer_churn
from app.core.config import settings

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/customer_churn")
async def predict(customer: Customer):
    return await predict_customer_churn(customer)