import yfinance as yf
import pandas as pd


def load_data():

    btc = yf.download(
        "BTC-USD",
        start="2020-01-01",
        progress=False
    )

    eth = yf.download(
        "ETH-USD",
        start="2020-01-01",
        progress=False
    )

    prices = pd.DataFrame({
        "BTC": btc["Close"],
        "ETH": eth["Close"]
    })

    return prices