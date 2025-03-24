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
    data = fetch_data(TICKER, YEARS_LOOKBACK)

    if "Adj Close" not in data.columns:
        print("❌ 'Adj Close' column not found.")
        return
    
    data = calculate_emas(data, EMA_SHORT, EMA_LONG)
    data = generate_signals(data, EMA_SHORT, EMA_LONG)

    signal_data = data[data["Buy Signals"].notna() | data["Sell Signals"].notna()]
    columns = ["Adj Close", f"EMA_{EMA_SHORT}", f"EMA_{EMA_LONG}", "Buy Signals", "Sell Signals"]
    signal_data[columns].to_csv(f"{TICKER}_signals_only.csv")
    print(f"📁 Exported buy/sell signals to {TICKER}_signals_only.csv")

    results = backtest_strategy(data)

    if not results.empty:
        print("\n📊 Backtest Results:")
        print(results)

        print("\n✅ Summary:")
        print(f"Total Trades: {len(results)}")
        print(f"Winning Trades: {sum(results['Profit'] > 0)}")
        print(f"Win Rate: {sum(results['Profit'] > 0) / len(results) * 100:.2f}%")
        print(f"Average Return per Trade: {results['Return (%)'].mean():.2f}%")
        print(f"Total Return: {results['Return (%)'].sum():.2f}%")

        results.to_csv(f"{TICKER}_backtest_results.csv", index=False)
        print(f"📁 Saved backtest results to {TICKER}_backtest_results.csv")
    else:
        print("No completed trades to evaluate.")

if __name__ == "__main__":
    main()