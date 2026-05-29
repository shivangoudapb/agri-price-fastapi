from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI(
    title="Agri Price Forecast API",
    version="1.0.0"
)

model = joblib.load(
    "price_forecast_model.pkl"
)

FEATURES = [
    'lag_1',
    'lag_2',
    'lag_3',
    'lag_6',
    'lag_12',
    'lag_24',
    'rolling_mean_3',
    'rolling_mean_6',
    'rolling_mean_12',
    'rolling_std_3',
    'rolling_std_6',
    'momentum_3',
    'month',
    'year'
]


@app.get("/")
def home():
    return {
        "message": "Agri Price Forecast API Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])

    df = df[FEATURES]

    prediction = model.predict(df)[0]

    return {
        "forecasted_price": float(prediction)
    }