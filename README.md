# Customer Churn Prediction App

This is Customer churn prediction App created using FastAPI and loads ML model to predict customer churn

## Requirements
Python 

## How to install and run
### Clone the repo:
```shell
git clone https://github.com/aditya-deshmukh-tech/customer-churn-end-to-end-ML-project
```

```shell
cd customer-churn-end-to-end-ML-project
```

### create virtual environment
```shell
python -m venv .venv
```

### Activate virtual environment (linux)
```shell
source .venv/bin/activate
```

### Activate virtual environment (windows)
```shell
.venv\Scripts\activate
```

### install dependencies
```shell
pip install -r requirements.txt
```

### run project
```shell
uvicorn app.main:app --reload --port 8080
```
