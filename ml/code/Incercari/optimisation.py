import pandas as pd
import numpy as np
import plotly.express as px
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

data = pd.read_csv("sales_and_eodStocksSheet1.csv", low_memory=False)
# print(data.head())

# Convert 'Product_ID' to numeric
data['Product_ID'] = pd.to_numeric(data['Product_ID'], errors='coerce')

# Filter the data for the specific product id
product_id = 10002  # replace with your product id
filtered_data = data[data['Product_ID'] == product_id]

# Convert the 'Date' column to datetime and set it as the index
filtered_data['Date'] = pd.to_datetime(filtered_data['Date'], format='%Y-%m-%d')
filtered_data.set_index('Date', inplace=True)

# Resample the data to daily frequency
filtered_data = filtered_data.resample('D').mean()
#
# # Forward fill any missing values
filtered_data = filtered_data.fillna(0)

# Truncate the data to the first 12 months
start_date = filtered_data.index.min()
end_date = start_date + pd.DateOffset(months=16)
filtered_data = filtered_data.truncate(before=start_date, after=end_date)

time_series = filtered_data['Sales']

differenced_series = time_series.diff().dropna()

# Plot ACF and PACF of differenced time series
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
plot_acf(differenced_series, ax=axes[0])
plot_pacf(differenced_series, ax=axes[1])
# plt.show()

order = (1, 1, 1)
seasonal_order = (1, 1, 1, 16) #12 because the data contains a time period of 2 months only
model = SARIMAX(time_series, order=order, seasonal_order=seasonal_order)
model_fit = model.fit(disp=False)

future_steps = 30
predictions = model_fit.predict(len(time_series), len(time_series) + future_steps - 1)
predictions = predictions.astype(int)
# print(predictions)

# Create date indices for the future predictions
future_dates = pd.date_range(start=time_series.index[-1] + pd.DateOffset(days=1), periods=future_steps, freq='D')

# Create a pandas Series with the predicted values and date indices
forecasted_demand = pd.Series(predictions, index=future_dates)
# print(forecasted_demand)

# Initial inventory level
# initial_inventory = 48704
#
# # Lead time (number of days it takes to replenish inventory)
# lead_time = 1 # it's different for every business, 1 is an example
#
# # Service level (probability of not stocking out)
# service_level = 0.95 # it's different for every business, 0.95 is an example
#
# # Calculate the optimal order quantity using the Newsvendor formula
# z = np.abs(np.percentile(forecasted_demand, 100 * (1 - service_level)))
# order_quantity = np.ceil(forecasted_demand.mean() + z).astype(int)
#
# # Calculate the reorder point
# reorder_point = forecasted_demand.mean() * lead_time + z
#
# # Calculate the optimal safety stock
# safety_stock = reorder_point - forecasted_demand.mean() * lead_time
#
# # Calculate the total cost (holding cost + stockout cost)
# holding_cost = 0.1  # it's different for every business, 0.1 is an example
# stockout_cost = 10  # # it's different for every business, 10 is an example
# total_holding_cost = holding_cost * (initial_inventory + 0.5 * order_quantity)
# total_stockout_cost = stockout_cost * np.maximum(0, forecasted_demand.mean() * lead_time - initial_inventory)
#
# # Calculate the total cost
# total_cost = total_holding_cost + total_stockout_cost
#
# print("Optimal Order Quantity:", order_quantity)
# print("Reorder Point:", reorder_point)
# print("Safety Stock:", safety_stock)
# print("Total Cost:", total_cost)
