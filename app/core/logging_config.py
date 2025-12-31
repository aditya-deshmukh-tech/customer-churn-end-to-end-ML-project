from logging.config import dictConfig
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOG_DIR = os.getenv("LOG_DIR", os.path.join(BASE_DIR, "logs"))
LOG_FILE = os.path.join(LOG_DIR, "app.log")

os.makedirs(LOG_DIR, exist_ok=True)

def setup_logging():
            dictConfig({
                "version": 1,
                "disable_existing_loggers": False,
                "formatters": {
                    "default": {
                        "format": "[%(asctime)s] %(levelname)s: in %(module)s: %(message)s",
                    },
                },
                "handlers": {
                    "console": {
                        "class": "logging.StreamHandler",
                        "formatter": "default",
                        "level": "INFO",
                        "stream": "ext://sys.stdout"
                    },
                    "file": {
                        "class": "logging.handlers.RotatingFileHandler",
                        "filename": LOG_FILE,
                        "level": "INFO",
                        "maxBytes": 1000000,
                        "backupCount": 3,
                        "formatter": "default",
                        "mode": "a",
                    }
                },
                "root": {
                    "level": "INFO",
                    "handlers": ["console", "file"],
                },
                "loggers": {
                    "uvicorn": {
                        "level": "INFO",
                        "handlers": ["console", "file"],
                        "propagate": False,
                    },
                    "uvicorn.error": {
                        "level": "INFO",
                        "handlers": ["console", "file"],
                        "propagate": False,
                    },
                    "uvicorn.access": {
                        "level": "INFO",
                        "handlers": ["console", "file"],
                        "propagate": False,
                    },
                }
            })
        