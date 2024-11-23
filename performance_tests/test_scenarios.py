from locust import TaskSet, task, between
import random
import json

class BrowsingBehavior(TaskSet):
    @task(3)
    def view_products(self):
        self.client.get("/api/products")
    
    @task(1)
    def search_products(self):
        search_terms = ["phone", "laptop", "tablet"]
        term = random.choice(search_terms)
        self.client.get(f"/api/products?search={term}")

class ShoppingBehavior(TaskSet):
    def on_start(self):
        self.cart_items = []
    
    @task(4)
    def add_to_cart(self):
        product_id = random.randint(1, 10)
        payload = {
            "product_id": product_id,
            "quantity": random.randint(1, 3)
        }
        with self.client.post("/api/orders", json=payload, catch_response=True) as response:
            if response.status_code == 200:
                self.cart_items.append(product_id)
                response.success()
            else:
                response.failure("Failed to add item to cart")

class UserBehavior(TaskSet):
    @task(2)
    def view_profile(self):
        user_id = random.randint(1, 100)
        self.client.get(f"/api/users/{user_id}")
    
    @task(1)
    def update_profile(self):
        user_id = random.randint(1, 100)
        payload = {
            "name": f"User {user_id}",
            "email": f"user{user_id}@example.com"
        }
        self.client.put(f"/api/users/{user_id}", json=payload)