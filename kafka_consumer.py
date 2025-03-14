from kafka import KafkaConsumer
import json
from transaction_processor import TransactionProcessor

consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

processor = TransactionProcessor()

for message in consumer:
    transaction = message.value
    processor.process_transaction(transaction)
    print(f"✅ Processed Transaction: {transaction}")
