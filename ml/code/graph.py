import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../csv/stocks.csv',low_memory=False)
data['Date'] = pd.to_datetime(data['Date'])
target_product_id_1 = str(20697)  

product_data_1 = data[data['Product_ID'] == target_product_id_1]

plt.figure(figsize=(12, 8))
plt.plot(product_data_1['Date'], product_data_1['Sales'])
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title(f"Sales across time for #{target_product_id_1}")
plt.grid(True)
plt.tight_layout()
plt.savefig('graph1.png')

target_product_id_2 = str(20765)  

product_data_2 = data[data['Product_ID'] == target_product_id_2]

plt.figure(figsize=(12, 8))
plt.plot(product_data_2['Date'], product_data_2['Sales'])
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title(f"Sales across time for #{target_product_id_2}")
plt.grid(True)
plt.tight_layout()
plt.savefig('graph2.png')

target_product_id_3 = str(20840)  

product_data_3 = data[data['Product_ID'] == target_product_id_3]

plt.figure(figsize=(12, 8))
plt.plot(product_data_3['Date'], product_data_3['Sales'])
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title(f"Sales across time for #{target_product_id_3}")
plt.grid(True)
plt.tight_layout()
plt.savefig('graph3.png')

target_product_id_4 = str(20857)  

product_data_4 = data[data['Product_ID'] == target_product_id_4]

plt.figure(figsize=(12, 8))
plt.plot(product_data_4['Date'], product_data_4['Sales'])
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title(f"Sales across time for #{target_product_id_4}")
plt.grid(True)
plt.tight_layout()
plt.savefig('graph4.png')

target_product_id_5 = str(20878)  

product_data_5 = data[data['Product_ID'] == target_product_id_5]

plt.figure(figsize=(12, 8))
plt.plot(product_data_5['Date'], product_data_5['Sales'])
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title(f"Sales across time for #{target_product_id_5}")
plt.grid(True)
plt.tight_layout()
plt.savefig('graph5.png')
