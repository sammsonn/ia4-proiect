import numpy as np
from prophet import Prophet
from scipy import stats
import pandas as pd
import warnings

from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
from statsmodels.tsa.statespace.sarimax import SARIMAX

warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv('sales_and_eodStocksSheet1.csv', low_memory=False)

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Filter out products that were sold only on one day in a year or sold few in total
data = data.groupby('Product_ID').filter(lambda x: len(x) > 1 and x['Sales'].sum() > 10)

def detect_anomalies(data):
    data['prev_stock'] = data['EndOfDayStock'].shift(1)
    stock_anomalies = data[(data['EndOfDayStock'] == data['prev_stock']) | (data['EndOfDayStock'] < data['Sales'])]
    return stock_anomalies

anomalies = detect_anomalies(data)

#drop column prev_stock
anomalies = anomalies.drop(columns=['prev_stock'])

#create another csv file with the data without anomalies
data = data.drop(anomalies.index)
data = data.drop(columns=['prev_stock'])

product_id = '10002'  # replace with your product id

filtered_data = data[data['Product_ID'] == product_id]

# Assuming 'filtered_data' is your DataFrame and 'Sales' is the column where you want to remove outliers
# z_scores = stats.zscore(filtered_data['Sales'])
# filtered_data = filtered_data[(z_scores < 3) & (z_scores > -3)]

# Convert the 'Date' column to datetime and set it as the index
# filtered_data['Date'] = pd.to_datetime(filtered_data['Date'], format='%Y-%m-%d')
filtered_data.set_index('Date', inplace=True)

# Resample the data to daily frequency
# filtered_data = filtered_data.resample('D').mean()

# Truncate the data to the first 12 months
start_date = filtered_data.index.min()
end_date = start_date + pd.DateOffset(months=12)
filtered_data = filtered_data.truncate(before=start_date, after=end_date)

time_series = filtered_data['Sales']

differenced_series = time_series.diff().dropna()

# Plot ACF and PACF of differenced time series
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
plot_acf(differenced_series, ax=axes[0])
plot_pacf(differenced_series, ax=axes[1])

order = (1, 1, 1)
seasonal_order = (1, 1, 1, 12) #12 because the data contains a time period of 2 months only
model = SARIMAX(time_series, order=order, seasonal_order=seasonal_order)
model_fit = model.fit(disp=False)

future_steps = 30
predictions = model_fit.predict(len(time_series), len(time_series) + future_steps - 1)
predictions = predictions.astype(int)
print(predictions)

# Create date indices for the future predictions
future_dates = pd.date_range(start=time_series.index[-1] + pd.DateOffset(days=1), periods=future_steps, freq='D')

# Create a pandas Series with the predicted values and date indices
forecasted_demand = pd.Series(predictions, index=future_dates)
print(forecasted_demand)