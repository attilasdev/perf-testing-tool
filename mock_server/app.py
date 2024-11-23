from fastapi import FastAPI, HTTPException
import time
import random

app = FastAPI()

@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    # Simulate varying response times
    time.sleep(random.uniform(0.1, 0.5))
    return {"user_id": user_id, "name": f"User {user_id}", "email": f"user{user_id}@example.com"}

@app.get("/api/products")
async def get_products():
    # Simulate heavy load
    time.sleep(random.uniform(0.2, 0.8))
    return [
        {"id": i, "name": f"Product {i}", "price": random.uniform(10, 100)}
        for i in range(1, 11)
    ]

@app.post("/api/orders")
async def create_order():
    # Simulate processing time
    time.sleep(random.uniform(0.3, 1.0))
    if random.random() < 0.1:  # 10% chance of failure
        raise HTTPException(status_code=500, detail="Internal server error")
    return {"order_id": random.randint(1000, 9999), "status": "created"}