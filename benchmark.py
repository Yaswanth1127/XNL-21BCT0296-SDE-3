import time
import cProfile
from src.transaction_processor import TransactionProcessor
from src.order_book import Order

def run_benchmark():
    processor = TransactionProcessor()
    orders = [Order(order_id=i, price=100, quantity=10, order_type='buy') for i in range(1000)]

    start_time = time.perf_counter()
    for order in orders:
        processor.process_transaction(order)
    end_time = time.perf_counter()

    print(f"✅ Benchmark Report: Processed 1000 orders in {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    run_benchmark()
    profiler.disable()
    profiler.print_stats(sort='time')
