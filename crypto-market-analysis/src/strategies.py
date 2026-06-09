def momentum_strategy(price):

    short_ma = price.rolling(20).mean()

    long_ma = price.rolling(50).mean()

    signal = (
        short_ma > long_ma
    ).astype(int)

    return signal

