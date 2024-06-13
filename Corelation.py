import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fetch historical data for Apple and Microsoft
start_date = '2023-01-01'
end_date = '2023-12-31'

aapl = yf.download('AAPL', start=start_date, end=end_date)
msft = yf.download('MSFT', start=start_date, end=end_date)

# Prepare the data
data = pd.DataFrame({
    'AAPL': aapl['Close'],
    'MSFT': msft['Close']
})

# Calculate daily returns
returns = data.pct_change().dropna()

# Calculate correlation
correlation = returns.corr().iloc[0, 1]
print(f"Correlation between AAPL and MSFT: {correlation}")

# Visualize the stock prices
plt.figure(figsize=(14, 7))
plt.subplot(2, 1, 1)
plt.plot(data['AAPL'], label='AAPL', color='blue')
plt.plot(data['MSFT'], label='MSFT', color='red')
plt.title('Stock Prices of AAPL and MSFT')
plt.legend()

# Visualize the returns
plt.subplot(2, 1, 2)
sns.regplot(x='AAPL', y='MSFT', data=returns, scatter_kws={'alpha':0.5})
plt.title('Daily Returns Correlation between AAPL and MSFT')

plt.tight_layout()
plt.show()
