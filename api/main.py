from fastapi import FastAPI
from pydantic import BaseModel
from .calculate import calculator

app = FastAPI()

class CalculationRequest(BaseModel):
    num1: float
    num2: float
    operation: str

@app.post("/calculate")
def calculate(input: CalculationRequest):
    result = calculator(input.num1, input.num2, input.operation)
    return {"result": result}
