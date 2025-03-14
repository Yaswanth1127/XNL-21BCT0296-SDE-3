import numpy as np

class PerformanceMetrics:
    @staticmethod
    def sharpe_ratio(returns, risk_free_rate=0.01):
        excess_returns = returns - risk_free_rate
        return np.mean(excess_returns) / np.std(excess_returns)

    @staticmethod
    def max_drawdown(portfolio_values):
        peak = portfolio_values.cummax()
        drawdown = (portfolio_values - peak) / peak
        return drawdown.min()

    @staticmethod
    def calculate_pnl(data):
        data['Returns'] = data['Close'].pct_change() * data['Signal'].shift(1)
        data['Cumulative_Return'] = (1 + data['Returns']).cumprod()
        return data
