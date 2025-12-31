import pickle
from fastapi import FastAPI
from app.api import health, customer_churn_api, customer_churn_ui
from app.core.logging_config import setup_logging
from app.services.model_store import load_ML_model, load_scalar_model

setup_logging()

app = FastAPI()

@app.on_event("startup")
def load_model():
    load_ML_model()
    load_scalar_model()


app.include_router(health.router, prefix="/api")
app.include_router(customer_churn_api.router, prefix="/api/v1")
app.include_router(customer_churn_ui.router, prefix="/ui")
        