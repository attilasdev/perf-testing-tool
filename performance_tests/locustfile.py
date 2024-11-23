from locust import HttpUser, task, between, events
import random
from reporting.report_generator import PerformanceReportGenerator
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PerformanceTestUser(HttpUser):
    wait_time = between(1, 3)
    
    def on_start(self):
        """Initialize user data before tests start"""
        self.test_data = {
            "user_ids": list(range(1, 101)),  # User IDs 1-100
            "order_payload": {
                "product_id": 1,
                "quantity": 1
            }
        }

    @task(3)
    def browse_products(self):
        """Test GET products endpoint"""
        with self.client.get("/api/products", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed to get products: {response.status_code}")

    @task(2)
    def view_user(self):
        """Test GET user endpoint"""
        user_id = random.choice(self.test_data["user_ids"])
        with self.client.get(
            f"/api/users/{user_id}",
            name="/api/users/[id]",
            catch_response=True
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed to get user: {response.status_code}")

    @task(1)
    def create_order(self):
        """Test POST order endpoint"""
        payload = self.test_data["order_payload"].copy()
        payload["quantity"] = random.randint(1, 5)
        
        with self.client.post(
            "/api/orders",
            json=payload,
            catch_response=True
        ) as response:
            if response.status_code in [200, 500]:  # 500 is expected occasionally
                response.success()
            else:
                response.failure(f"Unexpected status code: {response.status_code}")

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("Test is starting")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("Test is ending, generating report...")
    if environment.stats.total.num_requests > 0:
        reporter = PerformanceReportGenerator()
        reporter.generate_report(environment.stats)
    else:
        print("No requests were made during the test")

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    logger.info("Test is starting")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    logger.info("Test is ending, generating report...")
    logger.info(f"Total requests made: {environment.stats.total.num_requests}")
    logger.info(f"Number of entries: {len(environment.stats.entries)}")
    
    if environment.stats.total.num_requests > 0:
        try:
            reporter = PerformanceReportGenerator()
            reporter.generate_report(environment.stats)
            logger.info("Report generation completed")
        except Exception as e:
            logger.error(f"Error generating report: {str(e)}", exc_info=True)
    else:
        logger.warning("No requests were made during the test")