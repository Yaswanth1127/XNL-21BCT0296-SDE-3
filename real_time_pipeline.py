from kafka import KafkaProducer, KafkaConsumer
import json
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
import time
import random

# Kafka Configuration
KAFKA_TOPIC = "transactions"
KAFKA_SERVER = "localhost:9092"

# Load Pre-trained Fraud Detection Model
with open("models/xgboost_model.pkl", "rb") as model_file:
    fraud_model = pickle.load(model_file)

# Feature Scaling (Ensure consistency with model training)
scaler = StandardScaler()

# Producer: Simulate Real-Time Transactions
def produce_transactions():
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_SERVER,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    while True:
        transaction = {
            "transaction_id": random.randint(1000, 9999),
            "amount": round(random.uniform(10, 1000), 2),
            "currency": "USD",
            "timestamp": time.time(),
            "account_id": random.randint(1, 5000),
            "transaction_type": random.choice(["online", "in-store", "wire"]),
            "location": random.choice(["NY", "CA", "TX", "FL", "NV"]),
            "merchant_category": random.choice(["retail", "electronics", "gaming", "travel"])
        }
        producer.send(KAFKA_TOPIC, transaction)
        print(f"📤 Sent Transaction: {transaction}")
        time.sleep(1)  # Simulate real-time data feed (1 transaction per second)

# Consumer: Process Incoming Transactions & Fraud Detection
def consume_transactions():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_SERVER,
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for transaction in consumer:
        data = transaction.value
        
        # Convert data to DataFrame for prediction
        df = pd.DataFrame([data])
        features = df[['amount', 'account_id']]  # Add other relevant features here

        # Scale the data before prediction
        scaled_features = scaler.fit_transform(features)

        # Predict Fraud
        prediction = fraud_model.predict(scaled_features)[0]

        if prediction == 1:
            print(f"🚨 FRAUD ALERT: {data}")
        else:
            print(f"✅ Safe Transaction: {data}")

if __name__ == "__main__":
    choice = input("Choose [P]roducer or [C]onsumer: ").strip().lower()
    if choice == "p":
        produce_transactions()
    elif choice == "c":
        consume_transactions()
    else:
        print("❌ Invalid choice. Use 'P' or 'C'.")
