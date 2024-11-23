from fastapi import FastAPI, HTTPException, Query
from typing import Optional
import time
import random

app = FastAPI()

@app.get("/api/products")
async def get_products(search: Optional[str] = Query(None)):
    time.sleep(random.uniform(0.1, 0.5))
    products = [
        {"id": i, "name": f"Product {i}", "price": random.uniform(10, 100)}
        for i in range(1, 11)
    ]
    
    if search:
        products = [p for p in products if search.lower() in p["name"].lower()]
    
    return products

@app.put("/api/users/{user_id}")
async def update_user(user_id: int, user_data: dict):
    time.sleep(random.uniform(0.2, 0.6))
    if random.random() < 0.1:  # 10% chance of failure
        raise HTTPException(status_code=500, detail="Internal server error")
    return {"user_id": user_id, **user_data}