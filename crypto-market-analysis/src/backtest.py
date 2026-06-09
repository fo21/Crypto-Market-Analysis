strategy_returns = (
    signal.shift(1)
    * returns
)

equity = (1 + strategy_returns).cumprod()