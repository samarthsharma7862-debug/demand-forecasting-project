# 📊 Store Demand Forecasting Machine Learning Pipeline

An end-to-end Time-Series Machine Learning project built to predict a store's daily sales demand. This project leverages historical sales data, custom temporal feature engineering, and an optimized XGBoost Regressor to forecast stock requirements.

## 📂 Project Structure
* `data/` — Raw train, test, and cleaned store records.
* `models/` — Serialized production model weights (`best_xgb_model.pkl`).
* `notebooks/` — Dedicated development phases:
  * `01_eda.ipynb` — Data profiling, distribution analyses, and seasonality exploration.
  * `02_run_models.ipynb` — Feature engineering (7-day and 14-day rolling lags), model training, evaluation metrics, and validation.
  * `predict_future.py` — Standalone production inference script.

## 🛠️ Feature Engineering Highlight
To give our model a historical memory, we engineered deep temporal features:
* **Calendar Extraction:** `DayOfWeek`, `Month`, and `DayOfMonth` to track weekly and seasonal patterns.
* **Rolling Lags:** `Sales_Lag_7` and `Sales_Lag_14` to capture recent behavior trends from prior weeks.

## 🔮 7-Day Operational Forecast Results
The optimized XGBoost model successfully produced the following demand forecasts for the upcoming business cycle:

| Date | Day of the Week | Predicted Demand | Operational Action |
| :--- | :--- | :--- | :--- |
| **2015-08-01** | Saturday | **4,688 units** | Standard Weekend Restock |
| **2015-08-02** | Sunday | **154 units** | 📉 Low Activity / Structural Drawdown |
| **2015-08-03** | Monday | **5,116 units** | 🚀 Peak Surge Prep (High Stocking) |
| **2015-08-04** | Tuesday | **4,809 units** | High Baseline Maintenance |
| **2015-08-05** | Wednesday | **5,014 units** | High Baseline Maintenance |
| **2015-08-06** | Thursday | **4,777 units** | Standard Mid-week Stock |
| **2015-08-07** | Friday | **4,474 units** | Weekend Transition Supply |

*Note: The model correctly identified structural weekly drops (Sundays), protecting the business from excess holding overhead and product waste.*