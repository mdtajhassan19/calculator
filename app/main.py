from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class CalculatorRequest(BaseModel):
    a: float
    b: float
    operation: str

@app.post("/calculate")
def calculate(data: CalculatorRequest):
    if data.operation == "add":
        result = data.a + data.b
    elif data.operation == "sub":
        result = data.a - data.b
    elif data.operation == "mul":
        result = data.a * data.b
    elif data.operation == "div":
        if data.b == 0:
            raise HTTPException(status_code=400, detail="Division by zero not allowed in FastAPI calculator")
        result = data.a / data.b
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")

    return {"result": result}


# 👇 This replaces: uvicorn main:app --reload
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)