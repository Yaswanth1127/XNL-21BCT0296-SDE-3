# src/error_handler.py
from utils import log_error

class ErrorHandler:
    @staticmethod
    def handle_error(exception):
        log_error(f"Error encountered: {exception}")
