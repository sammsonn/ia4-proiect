import pandas as pd
from matplotlib import pyplot as plt
from prophet import Prophet
from prophet.plot import add_changepoints_to_plot
import plotly.express as px
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
from statsmodels.sandbox.distributions.examples.ex_mvelliptical import fig
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Load your data
# Make sure your date column is of datetime type
data = pd.read_csv('sales_and_eodStocksSheet1.csv', low_memory=False)

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Filter out products that were sold only on one day in a year or sold few in total
data = data.groupby('Product_ID').filter(lambda x: len(x) > 1 and x['Sales'].sum() > 10)

# Detect anomalies
def detect_anomalies(data):
    data['prev_stock'] = data['EndOfDayStock'].shift(1)
    stock_anomalies = data[(data['EndOfDayStock'] == data['prev_stock']) | (data['EndOfDayStock'] < data['Sales'])]
    return stock_anomalies

anomalies = detect_anomalies(data)

#drop column prev_stock
anomalies = anomalies.drop(columns=['prev_stock'])

# Write anomalies to a CSV file
# anomalies.to_csv('anomalii.csv', index=False)

#create another csv file with the data without anomalies
data = data.drop(anomalies.index)
data = data.drop(columns=['prev_stock'])
# data.to_csv('clean_data.csv', index=False)

df = data

product_id = '10002'  # replace with your product id
filtered_data = df[df['Product_ID'] == product_id]

# print(filtered_data.tail())

new_data = filtered_data[['Date', 'Sales']]
new_data = new_data.rename(columns={'Date': 'ds', 'Sales': 'y'})
# print(new_data.tail())


# Make the prophet model and fit on the data
model = Prophet(daily_seasonality=True, interval_width=0.95)
model.fit(new_data)

# Create future dates
future = model.make_future_dataframe(periods=30, freq='D')

# Predict sales
forecast = model.predict(future)

# forecast['yhat'] = forecast['yhat'].clip(lower=0)
# forecast['yhat_lower'] = forecast['yhat_lower'].clip(lower=0)
# forecast['yhat_upper'] = forecast['yhat_upper'].clip(lower=0)

# Plot the prediction
# plot1 = model.plot(forecast, uncertainty=True)
# a = add_changepoints_to_plot(fig.gca(), model, forecast)
# plt2 = model.plot_components(forecast)

# plt.show()

# Print the predictions
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(30))

# Convert 'ds' column to datetime in 'new_data'
# new_data['ds'] = pd.to_datetime(new_data['ds'])

# Assuming 'new_data' is your original dataset and 'forecast' is the prediction
# Merge the original data with the forecast
# merged = pd.merge(new_data, forecast, on='ds', how='inner')

# Calculate the error metrics
# mae = mean_absolute_error(merged['y'], merged['yhat'])
# mse = mean_squared_error(merged['y'], merged['yhat'])
# rmse = np.sqrt(mse)
# mape = np.mean(np.abs((merged['y'] - merged['yhat']) / merged['y'])) * 100
#
# print(f'MAE: {mae}')
# print(f'MSE: {mse}')
# print(f'RMSE: {rmse}')
# print(f'MAPE: {mape}%')
