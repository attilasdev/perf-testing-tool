from locust import HttpUser, task, between

class ApiUser(HttpUser):
    wait_time = between(1, 3)
    
    @task(3)
    def get_user(self):
        user_id = self.random_user_id()
        self.client.get(f"/api/users/{user_id}")
    
    @task(2)
    def get_products(self):
        self.client.get("/api/products")
    
    @task(1)
    def create_order(self):
        self.client.post("/api/orders")
    
    def random_user_id(self):
        return self.random.randint(1, 100)