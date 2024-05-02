

import streamlit as st
from prophet import Prophet
import pandas as pd
# Load your data (assuming df1 is defined somewhere)
# Replace this with your actual data loading code
df1 = pd.read_csv(r'C:\Users\pranu\Downloads\RELIANCE.NS(4).csv')

# Forecasting function
def run_forecast(df, periods):
    data = df.rename(columns={'Date': 'ds', 'Close': 'y'})
    model = Prophet()
    model.fit(data)
    future_dates = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future_dates)
    forecast_values = forecast[['ds', 'yhat']].tail(periods)
    return forecast_values

# Streamlit app code
def main():
    st.title('Prophet Forecasting App')
    st.write('This app forecasts the future values using Prophet Model.')
    
    # Get user input for forecast period
    periods = st.number_input('Enter the number of periods to forecast:', min_value=1, step=1, value=365)

    # Run forecast
    forecast_values = run_forecast(df1, periods)

    # Display forecasted values
    st.write(f'Forecast for the next {periods} periods:')
    st.write(forecast_values)

if __name__ == "__main__":
    main()