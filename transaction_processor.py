import asyncio
from order_book import Order, OrderBook
from collections import deque

class TransactionProcessor:
    def __init__(self):
        self.order_book = OrderBook()
        self.queue = asyncio.Queue()  # Queue for efficient transaction handling

    async def process_transaction(self):
        """Continuously processes transactions from the queue asynchronously."""
        while True:
            order = await self.queue.get()
            self.order_book.add_order(order)
            matches = self.order_book.match_orders()

            if matches:
                for match in matches:
                    print(f"✅ Transaction Match: Buy Order {match[0]} ↔️ Sell Order {match[1]} | Quantity: {match[2]}")
            
            self.queue.task_done()

    async def run_transaction_pipeline(self, transactions):
        """Add transactions to the queue for continuous processing."""
        for transaction in transactions:
            await self.queue.put(transaction)

        workers = [asyncio.create_task(self.process_transaction()) for _ in range(10)]
        await asyncio.gather(*workers)

# Sample Data for Testing
if __name__ == "__main__":
    processor = TransactionProcessor()

    sample_orders = [
        Order(order_id=1, price=100, quantity=10, order_type='buy'),
        Order(order_id=2, price=99, quantity=5, order_type='sell'),
        Order(order_id=3, price=100, quantity=15, order_type='buy'),
        Order(order_id=4, price=101, quantity=10, order_type='sell'),
        Order(order_id=5, price=102, quantity=20, order_type='buy'),
    ]

    asyncio.run(processor.run_transaction_pipeline(sample_orders))
