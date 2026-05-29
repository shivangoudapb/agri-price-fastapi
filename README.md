# Agricultural Price Forecast API

## Overview

This repository contains the backend prediction service for an Agricultural Price Forecasting System.

The service loads a trained XGBoost forecasting model and exposes prediction endpoints through FastAPI, enabling real-time agricultural price forecasting through REST APIs.

The model was trained using historical agricultural market price data and engineered time-series features including lag values, rolling statistics, and momentum indicators.

---

## Tech Stack

* Python
* FastAPI
* XGBoost
* Pandas
* Scikit-learn
* Joblib
* Render

---

## Model Features

The deployed model uses the following features:

* lag_1
* lag_2
* lag_3
* lag_6
* lag_12
* lag_24
* rolling_mean_3
* rolling_mean_6
* rolling_mean_12
* rolling_std_3
* rolling_std_6
* momentum_3
* month
* year

---

## API Endpoints

### GET /

Returns API status.

### GET /health

Returns service health information.

### POST /predict

Returns forecasted agricultural price.

Example Request:

```json
{
  "lag_1": 15000,
  "lag_2": 14800,
  "lag_3": 14500,
  "lag_6": 14000,
  "lag_12": 13000,
  "lag_24": 12000,
  "rolling_mean_3": 14766,
  "rolling_mean_6": 14400,
  "rolling_mean_12": 13600,
  "rolling_std_3": 250,
  "rolling_std_6": 400,
  "momentum_3": 500,
  "month": 10,
  "year": 2025
}
```

Example Response:

```json
{
  "forecasted_price": 14918.27
}
```

---

## Deployment

The FastAPI application is deployed on Render and serves predictions through a cloud-hosted REST API.

---

## Author

Shivangouda P Bhavihal
B.Tech Student
Machine Learning & Software Development Enthusiast
