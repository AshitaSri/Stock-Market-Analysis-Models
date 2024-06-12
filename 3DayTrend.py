import pandas as pd

# Sample data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'Close': [100, 102, 101, 105, 107, 110, 115, 117, 120, 125]
}
df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

# Calculate 3-day moving average
df['3_day_MA'] = df['Close'].rolling(window=3).mean()

# Calculate 3-day price change
df['3_day_Change'] = df['Close'].diff(periods=3)

# Calculate 3-day volatility
df['3_day_Volatility'] = df['Close'].rolling(window=3).std()

# Calculate 3-day momentum
df['3_day_Momentum'] = df['Close'] - df['Close'].shift(3)

print(df)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Drop NA values resulting from rolling calculations
df = df.dropna()

# Features and target
X = df[['3_day_MA', '3_day_Change', '3_day_Volatility', '3_day_Momentum']]
y = df['Close'].shift(-1).dropna()
X = X.iloc[:-1]  # Align features with target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = RandomForestRegressor()
model.fit(X_train_scaled, y_train)

# Predict and evaluate
y_pred = model.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
