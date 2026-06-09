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
    btc_close = btc[("Close", "BTC-USD")]
    eth_close = eth[("Close", "ETH-USD")]

    prices = pd.DataFrame({
        "BTC": btc_close,
        "ETH": eth_close
    })

    return prices