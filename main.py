# Trading-Bot to implement Algorithmic Trading Strategy
import datetime as dt 
import yfinance as yf 
import pandas as pd
from strategy import calculate_emas, generate_signals, backtest_strategy

TICKER = "NVDA"
EMA_SHORT = 30
EMA_LONG = 100
YEARS_LOOKBACK = 3

def fetch_data(ticker, years):
    start = dt.datetime.now() - dt.timedelta(days=365 * years)
    end = dt.datetime.now()
    data = yf.download(ticker, start=start, end=end, auto_adjust=False)

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.droplevel(1)

    return data

def main():
    pass