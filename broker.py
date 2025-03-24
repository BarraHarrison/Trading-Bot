import ccxt
import os
from dotenv import load_dotenv

load_dotenv()

def get_binance():
    return ccxt.binance({
        'apiKey': os.getenv("BINANCE_API_KEY"),
        'secret': os.getenv("BINANCE_SECRET_KEY"),
        'enableRateLimit': True,
    })

def place_order(exchange, symbol, side, amount):
    try:
        pass
    except Exception as e:
        pass