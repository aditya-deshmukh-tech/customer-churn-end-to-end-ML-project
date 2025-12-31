import pickle
import logging
from pathlib import Path

model = None
scalar = None

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "customer_churn_model.pkl"
scalar_path = BASE_DIR / "scaler.pkl"

logger = logging.getLogger(__name__)

def load_ML_model():
    global model

    if model is None:
        with open(MODEL_PATH, "rb") as f:
            logger.info("loading ML model....")
            model = pickle.load(f)
    return model


def load_scalar_model():
    global scalar

    if scalar is None:
        with open(scalar_path, "rb") as f:
            logger.info("loading scalar model....")
            scalar = pickle.load(f)
    return scalar

def get_model():
    if model is None:
        load_ML_model()
    return model

def get_scaler():
    if scalar is None:
        load_scalar_model()
    return scalar