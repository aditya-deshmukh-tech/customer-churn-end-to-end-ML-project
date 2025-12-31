from pydantic import BaseModel

class Customer(BaseModel):
    Age : int
    Gender : int
    Tenure : int
    Usage_Frequency : int
    Support_Calls : int
    Payment_Delay : int
    Total_Spend : int
    Last_Interaction : int
    Subscription_Type : str
    Contract_Length : str