from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_mock_transactions():
    """Generates random transaction data for real-time streaming."""
    while True:
        transaction = {
            "order_id": random.randint(1000, 9999),
            "price": round(random.uniform(95.0, 105.0), 2),
            "quantity": random.randint(1, 100),
            "order_type": random.choice(["buy", "sell"]),
        }
        producer.send('transactions', value=transaction)
        print(f"✅ Sent Transaction: {transaction}")
        time.sleep(1)

if __name__ == "__main__":
    generate_mock_transactions()
