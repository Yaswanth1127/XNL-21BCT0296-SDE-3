import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import cupy as cp  # GPU acceleration for numpy operations

class FraudDetector:
    def __init__(self, model_path="models/xgboost_model.pkl"):
        with open(model_path, "rb") as model_file:
            self.model = pickle.load(model_file)

    def predict_fraud(self, transaction_data):
        """Predicts if a transaction is fraudulent using GPU acceleration."""
        transaction_data = cp.asarray(transaction_data)  # GPU array conversion
        return self.model.predict(transaction_data)

# Sample Dataset
data = pd.read_csv("data/financial_transactions.csv")
X = data.drop(['is_fraud'], axis=1)
y = data['is_fraud']

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost Model with GPU Support
model = xgb.XGBClassifier(
    n_estimators=100,
    learning_rate=0.05,
    max_depth=5,
    tree_method='gpu_hist'  # Enables GPU acceleration
)
model.fit(X_train, y_train)

# Evaluate Model
y_pred = model.predict(X_test)
print(f"✅ Model Accuracy (GPU Optimized): {accuracy_score(y_test, y_pred):.2%}")

# Save Model
with open("models/xgboost_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)
    from cryptography.fernet import Fernet

# Generate & Save Key (One-time setup)
key = Fernet.generate_key()
with open("configs/encryption_key.key", "wb") as key_file:
    key_file.write(key)

# Encryption Logic
def encrypt_data(data):
    with open("configs/encryption_key.key", "rb") as key_file:
        cipher = Fernet(key_file.read())
    return cipher.encrypt(data.encode())

def decrypt_data(encrypted_data):
    with open("configs/encryption_key.key", "rb") as key_file:
        cipher = Fernet(key_file.read())
    return cipher.decrypt(encrypted_data).decode()

