#!/usr/bin/env python
# coding: utf-8

# In[3]:


import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ta
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# For plotting inline in Jupyter
get_ipython().run_line_magic('matplotlib', 'inline')


# # Download historical stock prices

# In[4]:


# Define the stock symbol and the time period
symbol = 'AAPL'
start_date = '2010-01-01'
end_date = '2023-01-01'

# Download the data
data = yf.download(symbol, start=start_date, end=end_date)

# Display the first few rows
data.head()


# # Calculating Financial Indicator

# In[5]:


# Create a copy of the data
df = data.copy()

# Calculate Relative Strength Index (RSI)
df['RSI'] = ta.momentum.rsi(df['Adj Close'], window=14)


# Drop any rows with NaN values (optional)
df.dropna(inplace=True)

# Display the first few rows with indicators
df.head()


# In[17]:


# Filter data for the last 6 months
last_six_months = df.loc[df.index >= (pd.to_datetime(end_date) - pd.DateOffset(months=6))]

# Plot the Close Price and RSI
fig, (ax1, ax2) = plt.subplots(2, figsize=(14, 10), sharex=True)

# Plot Close Price
ax1.plot(last_six_months.index, last_six_months['Adj Close'], label='Close Price', color='blue')
ax1.set_title('AAPL Close Price (Last 6 Months)')
ax1.set_ylabel('Price')
ax1.legend()
ax1.grid(True)

# Plot RSI
ax2.plot(last_six_months.index, last_six_months['RSI'], label='RSI', color='orange')
ax2.axhline(70, linestyle='--', alpha=0.5, color='red', label='Overbought (70)')
ax2.axhline(30, linestyle='--', alpha=0.5, color='green', label='Oversold (30)')
ax2.set_title('Relative Strength Index (RSI) (Last 6 Months)')
ax2.set_ylabel('RSI')
ax2.legend()
ax2.grid(True)

plt.show()


# In[ ]:





# In[ ]:




