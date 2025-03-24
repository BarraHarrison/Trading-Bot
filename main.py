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
    pass

def main():
    pass