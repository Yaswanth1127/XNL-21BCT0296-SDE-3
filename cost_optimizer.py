# src/cost_optimizer.py
from utils import log_info

class CostOptimizer:
    def __init__(self, strategy="VWAP"):
        self.strategy = strategy

    def optimize_cost(self, order_book):
        optimal_price = sum(order['price'] for order in order_book) / len(order_book)
        log_info(f"Optimal price for {self.strategy} strategy: {optimal_price}")
        return optimal_price
