import pandas as pd
import numpy as np

class TradingStrategy:
    def __init__(self, data):
        self.data = data

    # RSI Strategy
    def rsi_strategy(self, period=14, overbought=70, oversold=30):
        delta = self.data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

        rs = gain / loss
        self.data['RSI'] = 100 - (100 / (1 + rs))

        self.data['Signal'] = np.where(self.data['RSI'] < oversold, 1, 0)  # Buy Signal
        self.data['Signal'] = np.where(self.data['RSI'] > overbought, -1, self.data['Signal'])  # Sell Signal
        return self.data

    # MACD Strategy
    def macd_strategy(self, short_window=12, long_window=26, signal_window=9):
        self.data['EMA12'] = self.data['Close'].ewm(span=short_window).mean()
        self.data['EMA26'] = self.data['Close'].ewm(span=long_window).mean()
        self.data['MACD'] = self.data['EMA12'] - self.data['EMA26']
        self.data['Signal'] = self.data['MACD'].ewm(span=signal_window).mean()

        self.data['Trade_Signal'] = np.where(self.data['MACD'] > self.data['Signal'], 1, -1)
        return self.data
