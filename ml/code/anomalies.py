import pandas as pd

# Load data
data = pd.read_csv('../csv/stockuri produse ia4.csv')

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
anomalies.to_csv('../csv/anomalii.csv', index=False)

#create another csv file with the data without anomalies
data = data[~data['Product_ID'].isin(anomalies['Product_ID'])]
data.to_csv('../csv/clean_data.csv', index=False)


# create a plot with top 10 anomalies
import matplotlib.pyplot as plt
import seaborn as sns

top_anomalies = anomalies.groupby('Product_ID').agg({'Sales': 'sum'}).sort_values(by='Sales', ascending=False).head(10)
top_anomalies = top_anomalies.reset_index()

top_anomalies = pd.merge(top_anomalies, anomalies, on='Product_ID', how='left')

sns.set_style('whitegrid')
plt.figure(figsize=(12, 8))
sns.barplot(x='Product_ID', y='Sales_x', data=top_anomalies)
plt.title('Top anomalies')
plt.xlabel('Product ID')
plt.ylabel('Sales')
plt.savefig('top_anomalies.png')
plt.show()

# create a graph with the sales in tme of product id 20697
product_20697 = data[data['Product_ID'] == 20697]
product_20697 = product_20697[['Date', 'Sales']]
product_20697 = product_20697.set_index('Date')

sns.set_style('whitegrid')
plt.figure(figsize=(12, 8))
sns.lineplot(data=product_20697, x='Date', y='Sales')
plt.title('Product 20697')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.savefig('product_20697.png')
plt.show()
