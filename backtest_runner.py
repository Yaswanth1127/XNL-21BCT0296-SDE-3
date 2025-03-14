import pandas as pd
from strategy_engine import TradingStrategy
from performance_metrics import PerformanceMetrics

class BacktestRunner:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path, parse_dates=['Date'], index_col='Date')

    def run_backtest(self, strategy_type='rsi'):
        strategy = TradingStrategy(self.data)

        if strategy_type == 'rsi':
            self.data = strategy.rsi_strategy()
        elif strategy_type == 'macd':
            self.data = strategy.macd_strategy()

        # Calculate Performance
        self.data = PerformanceMetrics.calculate_pnl(self.data)

        sharpe_ratio = PerformanceMetrics.sharpe_ratio(self.data['Returns'])
        max_drawdown = PerformanceMetrics.max_drawdown(self.data['Cumulative_Return'])

        print(f"📊 Sharpe Ratio: {sharpe_ratio:.2f}")
        print(f"📉 Max Drawdown: {max_drawdown:.2%}")

if __name__ == "__main__":
    runner = BacktestRunner('data/historical_data.csv')
    runner.run_backtest(strategy_type='rsi')
