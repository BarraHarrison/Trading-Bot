# Trading-Bot to implement Algorithmic Trading Strategy
import datetime as dt 
import yfinance as yf 
import pandas as pd
from strategy import calculate_emas, generate_signals, backtest_strategy
