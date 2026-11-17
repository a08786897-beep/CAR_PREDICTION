from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

app = FastAPI(title="Car Price Prediction API")

# Enable CORS taaki frontend easily communicate kar sake
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for incoming request data
# (Features tune jo diye hain: model, year, transmission, mileage, fuelType, tax, mpg, engineSize)
class CarFeatures(BaseModel):
    model_name: str
    year: int
    transmission: str
    mileage: float
    fuelType: str
    tax: float
    mpg: float
    engineSize: float

# Model aur scaler load karne ka code (apni .pkl files ka sahi naam yahan daal dena)
try:
    # Example: model = joblib.load('car_model.pkl')
    # scaler = joblib.load('scaler.pkl')
    pass
except Exception as e:
    print(f"Warning: Model files not loaded yet. Error: {e}")

@app.post("/predict")
def predict_price(data: CarFeatures):
    try:
        # Yahan apna prediction logic likhna jo model aur scaler use kare
        # Dummy response for demonstration:
        input_data = pd.DataFrame([data.dict()])
        
        # Mock calculation based on year & mileage for testing UI if model isn't hooked yet
        base_price = 500000 
        predicted_price = base_price + (data.year * 1000) - (data.mileage * 2)
        
        return {
            "status": "success",
            "predicted_price_inr": round(float(predicted_price), 2)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)