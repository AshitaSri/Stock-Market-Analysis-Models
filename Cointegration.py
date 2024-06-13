import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import coint

# Fetch historical data for two stocks
start_date = '2022-01-01'
end_date = '2023-01-01'

stock1 = yf.download('AAPL', start=start_date, end=end_date)
stock2 = yf.download('MSFT', start=start_date, end=end_date)

# Prepare the data
prices = pd.DataFrame({
    'AAPL': stock1['Close'],
    'MSFT': stock2['Close']
})

# Test for co-integration
coint_result = coint(prices['AAPL'], prices['MSFT'])
p_value = coint_result[1]
print(f"P-value for co-integration test: {p_value}")

# Interpret the result
if p_value < 0.05:
    print("The time series are co-integrated.")
else:
    print("The time series are not co-integrated.")

# Visualize the stock prices and spread
plt.figure(figsize=(14, 7))

# Plot stock prices
plt.subplot(2, 1, 1)
plt.plot(prices['AAPL'], label='AAPL')
plt.plot(prices['MSFT'], label='MSFT')
plt.legend()
plt.title('Stock Prices of AAPL and MSFT')

# Plot the spread
spread = prices['AAPL'] - prices['MSFT']
plt.subplot(2, 1, 2)
plt.plot(spread, label='AAPL - MSFT')
plt.axhline(spread.mean(), color='red', linestyle='--')
plt.legend()
plt.title('Spread between AAPL and MSFT')

plt.tight_layout()
plt.show()
