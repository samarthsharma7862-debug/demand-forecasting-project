# 📊 Store Demand Forecasting Machine Learning Pipeline

An end-to-end Time-Series Machine Learning project built to predict a store's daily sales demand. This project leverages historical sales data, custom temporal feature engineering, and an optimized XGBoost Regressor to forecast stock requirements.

## 📈 Model Performance
| Metric | Baseline XGBoost | Tuned XGBoost (GridSearchCV) |
|--------|-----------------|------------------------------|
| RMSE   | 952.35          | 913.33                       |
| MAE    | 520.37          | 486.22                       |
| R²     | 0.7267          | 0.7486                       |

**Best Params:** `learning_rate=0.1, max_depth=3, n_estimators=300`

## 📂 Project Structure
```
demand-forecasting-project/
│
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── store1_clean.csv
│
├── models/
│   └── best_xgb_model.pkl
│
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_run_models.ipynb
│
├── predict_future.py
├── requirements.txt
└── README.md
```

## 🛠️ Feature Engineering
- **Calendar Features:** `DayOfWeek`, `Month`, `DayOfMonth` to capture weekly and seasonal patterns
- **Lag Features:** `Sales_Lag_7` and `Sales_Lag_14` to give the model memory of recent sales behavior

## 🔮 7-Day Operational Forecast Results
| Date | Day | Predicted Demand | Action |
|------|-----|-----------------|--------|
| 2015-08-01 | Saturday | 4,688 units | Standard Weekend Restock |
| 2015-08-02 | Sunday | 154 units | 📉 Low Activity / Structural Drawdown |
| 2015-08-03 | Monday | 5,116 units | 🚀 Peak Surge Prep |
| 2015-08-04 | Tuesday | 4,809 units | High Baseline Maintenance |
| 2015-08-05 | Wednesday | 5,014 units | High Baseline Maintenance |
| 2015-08-06 | Thursday | 4,777 units | Standard Mid-week Stock |
| 2015-08-07 | Friday | 4,474 units | Weekend Transition Supply |

## ⚙️ How to Run
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run EDA notebook: `notebooks/01_eda.ipynb`
4. Run model training: `notebooks/02_run_models.ipynb`
5. Run future forecast:
```bash
python predict_future.py
```

## 🧰 Tech Stack
- Python 3.13
- XGBoost
- scikit-learn (GridSearchCV)
- pandas, numpy
- matplotlib, statsmodels, joblib
