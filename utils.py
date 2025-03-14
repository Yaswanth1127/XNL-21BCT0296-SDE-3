import numpy as np
from sklearn.ensemble import IsolationForest

class FraudDetection:
    def __init__(self):
        # Initialize Isolation Forest model for anomaly detection
        self.model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)

    def train_model(self, transaction_data):
        """
        Train the Isolation Forest model on historical transaction data.
        """
        features = self._extract_features(transaction_data)
        self.model.fit(features)
        print("✅ Fraud detection model trained successfully!")

    def predict(self, transactions):
        """
        Predict if transactions are fraudulent.
        """
        features = self._extract_features(transactions)
        predictions = self.model.predict(features)
        return [
            {"id": transaction['id'], "is_fraud": pred == -1}
            for transaction, pred in zip(transactions, predictions)
        ]

    def _extract_features(self, transactions):
        """
        Extracts numerical features from transaction data for model training and prediction.
        """
        return np.array([
            [transaction['amount'], 1 if transaction['type'] == 'credit' else 0]
            for transaction in transactions
        ])
