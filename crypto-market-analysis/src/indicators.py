from data_loader import load_data

prices = load_data()

returns = prices.pct_change().dropna()

returns.describe()