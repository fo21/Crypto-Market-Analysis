import seaborn as sns
import matplotlib.pyplot as plt

from data_loader import load_data

prices = load_data()

returns = prices.pct_change().dropna()

print(returns.describe())

corr = returns.corr()

print(corr)

sns.heatmap(
    corr,
    annot=True
)

plt.show()

volatility = returns.std() * (365 ** 0.5)

print(volatility)