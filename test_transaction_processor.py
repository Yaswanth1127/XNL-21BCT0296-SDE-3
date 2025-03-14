import unittest
from src.transaction_processor import TransactionProcessor
from src.order_book import Order

class TestTransactionProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = TransactionProcessor()

    def test_single_transaction(self):
        order = Order(order_id=1, price=100, quantity=10, order_type='buy')
        self.processor.process_transaction(order)
        self.assertEqual(len(self.processor.order_book.buy_orders), 1)

    def test_transaction_matching(self):
        buy_order = Order(order_id=1, price=100, quantity=10, order_type='buy')
        sell_order = Order(order_id=2, price=100, quantity=10, order_type='sell')

        self.processor.process_transaction(buy_order)
        self.processor.process_transaction(sell_order)

        self.assertEqual(len(self.processor.order_book.buy_orders), 0)
        self.assertEqual(len(self.processor.order_book.sell_orders), 0)

if __name__ == '__main__':
    unittest.main()
