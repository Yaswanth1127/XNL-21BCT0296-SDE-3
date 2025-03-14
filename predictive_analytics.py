# src/predictive_analytics.py
import numpy as np
from keras.models import load_model
from utils import log_info

class PredictiveAnalytics:
    def __init__(self):
        self.model = load_model("models/lstm_market_trend_model.h5")

    def predict_trend(self, historical_data):
        prediction = self.model.predict(np.array([historical_data]))[0]
        trend = "Bullish" if prediction > 0.5 else "Bearish"
        log_info(f"Market prediction: {trend}")
        return trend
