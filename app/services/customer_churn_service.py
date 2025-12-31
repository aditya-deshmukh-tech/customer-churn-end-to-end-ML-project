from app.models.model_objs import Customer
from .model_store import get_model, get_scaler
import pandas as pd

def subscription_to_dict(subscription_type: str) -> dict:
    types = ["Subscription_Type_Basic", "Subscription_Type_Premium", "Subscription_Type_Standard"]
    return {t: 1 if t == subscription_type else 0 for t in types}

def contract_length_to_dict(contract_length: str) -> dict:
    types = ["Contract_Length_Annual", "Contract_Length_Monthly", "Contract_Length_Quarterly"]
    return {t: 1 if t == contract_length else 0 for t in types}

def get_prediction_values_array(customer: Customer):
    final_predict_dict = customer.model_dump()

    sub_type_dict = subscription_to_dict(final_predict_dict["Subscription_Type"])

    contract_dict = contract_length_to_dict(final_predict_dict["Contract_Length"])

    final_predict_dict.update(sub_type_dict)

    final_predict_dict.update(contract_dict)

    final_predict_dict.pop("Subscription_Type")

    final_predict_dict.pop("Contract_Length")

    return [final_predict_dict]

columns = ["Age", "Gender", "Tenure", "Usage_Frequency", "Support_Calls", "Payment_Delay", "Total_Spend", "Last_Interaction", "Subscription_Type_Basic", "Subscription_Type_Premium", "Subscription_Type_Standard", "Contract_Length_Annual", "Contract_Length_Monthly", "Contract_Length_Quarterly"]

async def predict_customer_churn(customer: Customer):
    scalar = get_scaler()
    model = get_model()
    df = pd.DataFrame(get_prediction_values_array(customer))
    df = df.reindex(columns=columns)
    customer_data_scaled = scalar.transform(df)
    prediction = model.predict(customer_data_scaled)
    print("Prediction:", prediction[0])
    return {"customer_can_left" : True} if prediction[0] == 1 else {"customer_can_left" : False}