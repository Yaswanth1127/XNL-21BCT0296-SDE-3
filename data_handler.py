import pandas as pd
import numpy as np

class DataHandler:
    def __init__(self, batch_size=100):
        self.batch_size = batch_size

    def load_data_in_batches(self, file_path):
        """Load data efficiently in batches for reduced latency."""
        for batch in pd.read_csv(file_path, chunksize=self.batch_size):
            yield batch

    def preprocess_data(self, batch):
        """Efficient data cleaning and transformation for better processing speed."""
        batch.fillna(0, inplace=True)
        return batch.astype(np.float32)

# Example Usage
if __name__ == "__main__":
    handler = DataHandler(batch_size=500)
    for batch in handler.load_data_in_batches("data/financial_transactions.csv"):
        processed_batch = handler.preprocess_data(batch)
        print(f"✅ Processed Batch with {len(processed_batch)} records")
