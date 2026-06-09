def momentum_strategy(price):

    short_ma = price.rolling(20).mean()

    long_ma = price.rolling(50).mean()

    signal = (
        short_ma > long_ma
    ).astype(int)

    return signal

def mean_reversion(price):

    rolling_mean = price.rolling(20).mean()

    rolling_std = price.rolling(20).std()

    zscore = (
        price - rolling_mean
    ) / rolling_std

    signal = (zscore < -1).astype(int)

    return signal