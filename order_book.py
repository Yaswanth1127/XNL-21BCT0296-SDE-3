import threading
import heapq
from collections import defaultdict
import time

class Order:
    def __init__(self, order_id, price, quantity, order_type, timestamp=None):
        self.order_id = order_id
        self.price = price
        self.quantity = quantity
        self.order_type = order_type  # "buy" or "sell"
        self.timestamp = timestamp or time.time()

    def __lt__(self, other):
        if self.order_type == 'buy':
            return self.price > other.price  # Higher price first for buy orders
        else:
            return self.price < other.price  # Lower price first for sell orders

class OrderBook:
    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []
        self.lock = threading.Lock()

    def add_order(self, order):
        with self.lock:
            if order.order_type == "buy":
                heapq.heappush(self.buy_orders, order)
            elif order.order_type == "sell":
                heapq.heappush(self.sell_orders, order)

    def match_orders(self):
        with self.lock:
            matched_orders = []
            while self.buy_orders and self.sell_orders:
                best_buy = self.buy_orders[0]  # Highest buy price
                best_sell = self.sell_orders[0]  # Lowest sell price

                if best_buy.price >= best_sell.price:
                    # Transaction occurs
                    matched_qty = min(best_buy.quantity, best_sell.quantity)
                    matched_orders.append((best_buy.order_id, best_sell.order_id, matched_qty))

                    # Update or remove orders
                    if best_buy.quantity == matched_qty:
                        heapq.heappop(self.buy_orders)
                    else:
                        self.buy_orders[0].quantity -= matched_qty

                    if best_sell.quantity == matched_qty:
                        heapq.heappop(self.sell_orders)
                    else:
                        self.sell_orders[0].quantity -= matched_qty
                else:
                    break  # No match possible

            return matched_orders
