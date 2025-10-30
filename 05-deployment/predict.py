import pickle
from fastapi import FastAPI
from typing import Literal
import uvicorn
from pydantic import BaseModel, Field

class Data(BaseModel): 
    lead_source: Literal["paid_ads", "organic_search"]
    number_of_courses_viewed: int
    annual_income: float

class PredictResponse(BaseModel):
    convert_probability: float
    convert: bool

model_file_name = "pipeline_v2.bin"

app = FastAPI(title="customer-churn-prediction")

with open(model_file_name, 'rb') as f_in:
    pipeline = pickle.load(f_in)


def predict_single(data):
    result = pipeline.predict_proba(data)[0, 1]
    return float(result)


@app.post("/predict")
def predict(data: Data) -> PredictResponse:
    prob = predict_single(data.model_dump())

    return PredictResponse(
        convert_probability=prob,
        convert=prob >= 0.5
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9697)