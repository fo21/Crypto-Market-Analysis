import numpy as np


def sharpe_ratio(strategy_returns):

    return (
        strategy_returns.mean()
        /
        strategy_returns.std()
    ) * np.sqrt(365)

def max_drawdown(equity):

    peak = equity.cummax()

    drawdown = (
        equity - peak
    ) / peak

    return drawdown.min()