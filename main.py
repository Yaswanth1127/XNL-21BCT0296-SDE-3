# main.py
from src.transaction_processor import TransactionProcessor
from src.fraud_detection import FraudDetector
from src.predictive_analytics import PredictiveAnalytics
from src.risk_management import RiskManager
from src.cost_optimizer import CostOptimizer
from src.error_handler import ErrorHandler

try:
    processor = TransactionProcessor(max_threads=10)
    fraud_detector = FraudDetector()
    analytics = PredictiveAnalytics()
    risk_manager = RiskManager()
    cost_optimizer = CostOptimizer()

    sample_transaction = {"id": 1, "amount": 500, "frequency": 3, "location_score": 0.9}

    processor.add_transaction(sample_transaction)
    processor.run()

    fraud_detector.detect_fraud(sample_transaction)
    analytics.predict_trend([1, 2, 3, 4, 5])
    risk_manager.assess_risk(sample_transaction)
    cost_optimizer.optimize_cost([{"price": 100}, {"price": 200}])

except Exception as e:
    ErrorHandler.handle_error(e)
