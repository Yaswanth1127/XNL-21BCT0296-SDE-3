# src/logger.py
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_info(message):
    logging.info(message)

def log_warning(message):
    logging.warning(message)

def log_error(message):
    logging.error(message)
from loguru import logger

logger.add("logs/transaction_processor.log", rotation="10 MB", level="INFO")

def process_transaction(transaction):
    try:
        # Transaction logic
        logger.info(f"Transaction {transaction['id']} processed successfully.")
    except Exception as e:
        logger.error(f"Transaction Failed: {e}")
