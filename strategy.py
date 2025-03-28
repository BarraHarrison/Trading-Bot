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
    """
    Generate buy/sell signals based on EMA crossover strategy.
    
    Parameters:
        data (pd.DataFrame): Data with calculated EMAs.
        short (int): Short-term EMA period.
        long (int): Long-term EMA period.
    
    Returns:
        pd.DataFrame: Data with 'Buy Signals' and 'Sell Signals' columns added.
    """
    buy_signals, sell_signals = [], []
    trigger = 0

    for i in range(len(data)):
        ema_short = data[f"EMA_{short}"].iloc[i]
        ema_long = data[f"EMA_{long}"].iloc[i]
        close_price = data["Adj Close"].iloc[i]

        if ema_short > ema_long and trigger != 1:
            buy_signals.append(close_price)
            sell_signals.append(float("nan"))
            trigger = 1
        elif ema_short < ema_long and trigger != 1:
            buy_signals.append(float("nan"))
            sell_signals.append(close_price)
            trigger = -1
        else:
            buy_signals.append(float("nan"))
            sell_signals.append(float("nan"))

    data["Buy Signals"] = buy_signals
    data["Sell Signals"] = sell_signals
    return data

def backtest_strategy(data):
    """
    Backtest strategy based on the generated buy/sell signals.

    Parameters:
        data (pd.DataFrame): Data with 'Buy Signals' and 'Sell Signals' columns.

    Returns:
        pd.DataFrame: Trade history with performance metrics.
    """
    positions = []
    entry_price = None
    trade_returns = []

    for i in range(len(data)):
        row = data.iloc[i]

        if not pd.isna(row["Buy Signals"]) and entry_price is None:
            entry_price = row["Buy Signals"]
            entry_date = row.name

        elif not pd.isna(row["Sell Signals"]) and entry_price is not None:
            exit_price = row["Sell Signals"]
            exit_date = row.name

            profit = exit_price - entry_price
            return_pct = (profit /entry_price) * 100

            positions.append({
                "Entry Date": entry_date,
                "Exit Date": exit_date,
                "Entry Price": entry_price,
                "Exit Price": exit_price,
                "Profit": profit,
                "Return (%)": return_pct
            })

            trade_returns.append(return_pct)
            entry_price = None

    return pd.DataFrame(positions)