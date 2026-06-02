import joblib
import pandas as pd
import numpy as np

def generate_future_predictions():
    # 1. Load the trained production model safely
    model_path = 'models/best_xgb_model.pkl'
    try:
        model = joblib.load(model_path)
        print("✨ Production Model Loaded Successfully!")
    except FileNotFoundError:
        print(f"❌ Error: Could not find the saved model at {model_path}. Make sure to run your notebook first.")
        return

    # 2. Simulate incoming new data for next week (7 days)
    print("\n🔮 Generating Forecasts for the Next 7 Days...")
    future_dates = pd.date_range(start='2015-08-01', periods=7, freq='D')

    # 3. Create the exact matching feature matrix structure
    future_df = pd.DataFrame(index=future_dates)
    future_df['DayOfWeek'] = future_df.index.dayofweek
    future_df['Month'] = future_df.index.month
    future_df['DayOfMonth'] = future_df.index.day

    # Mock recent lag values (simulating the last known week of sales)
    future_df['Sales_Lag_7'] = [4100, 3800, 3900, 4200, 5100, 6000, 3200]
    future_df['Sales_Lag_14'] = [4000, 3750, 3850, 4100, 5000, 5900, 3100]

    # 4. Generate the predictions
    features = future_df[['DayOfWeek', 'Month', 'DayOfMonth', 'Sales_Lag_7', 'Sales_Lag_14']]
    future_df['Forecasted_Sales'] = model.predict(features)

    # 5. Display the clean output table
    print("\n📋 Final Demand Forecast Results:")
    print("-" * 45)
    for date, row in future_df.iterrows():
        print(f"Date: {date.date()} | Day: {date.day_name():10} | Predicted Demand: {int(row['Forecasted_Sales'])} units")
    print("-" * 45)

if __name__ == "__main__":
    generate_future_predictions()