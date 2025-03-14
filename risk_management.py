# src/risk_management.py
import numpy as np
from utils import log_info

class RiskManager:
    def __init__(self, threshold=0.7):
        self.threshold = threshold

    def calculate_var(self, portfolio):
        returns = np.random.normal(0.001, 0.02, 1000)
        var = np.percentile(returns, 5)
        log_info(f"Calculated Value-at-Risk (VaR): {var}")
        return var

    def assess_risk(self, portfolio):
        risk_score = self.calculate_var(portfolio)
        return "High Risk" if risk_score > self.threshold else "Low Risk"
