from data_loader import load_data

prices = load_data()

returns = prices.pct_change().dropna()

print(returns.describe())

corr = returns.corr()

print(corr)