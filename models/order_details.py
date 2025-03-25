from pydantic import BaseModel
from datetime import datetime

class OrderDetail(BaseModel):
    customer_name: str
    product_name: str
    quantity: int
    price: float
    date_time: datetime


