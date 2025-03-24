# Algorithmic Trading Strategy
import pandas as pd

def calculate_emas(data, short=30, long=100):
    """
    Calculate Exponential Moving Averages (EMAs) and add them to the DataFrame.
    
    Parameters:
        data (pd.DataFrame): Stock data with 'Adj Close' prices.
        short (int): Short-term EMA period.
        long (int): Long-term EMA period.
    
    Returns:
        pd.DataFrame: Data with EMA columns added and trimmed to valid EMA range.
    """
    data[f"EMA_{short}"] = data["Adj Close"].ewm(span=short, adjust=False).mean()
    data[f"EMA_{long}"] = data["Adj Close"].ewm(span=long, adjust=False).mean()
    return data.iloc[long:]

def generate_signals(data, short=30, long=100):
    pass

def backtest_strategy(data):
    pass