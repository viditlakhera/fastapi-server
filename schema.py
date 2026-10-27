from pydantic import BaseModel

class productcreate(BaseModel):
    name: str
    description: str
    quantity: int
    price: float
    