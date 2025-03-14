from locust import HttpUser, task, between

class TransactionLoadTest(HttpUser):
    wait_time = between(0.5, 1.5)

    @task
    def simulate_transactions(self):
        self.client.post("/transaction", json={
            "order_id": 1,
            "price": 100,
            "quantity": 10,
            "order_type": "buy"
        })
