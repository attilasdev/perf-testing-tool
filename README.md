# Performance Testing Tool

A comprehensive performance testing framework built with Locust, featuring real-time monitoring, custom reporting, and configurable test scenarios.

> **Note**: This is a learning portfolio project created to demonstrate performance testing concepts and Python development skills. It's not intended for production use but rather as an educational resource and skill showcase.

## Project Overview

This project serves as a practical example of:
- Building scalable performance testing frameworks
- Implementing monitoring and reporting systems
- Working with modern Python testing tools
- Creating maintainable and documented code
- Developing mock servers for testing
## Project Structure

```plaintext
perf-testing-tool/
├── mock_server/
│   └── app.py                 # FastAPI mock server
├── monitoring/
│   └── resource_monitor.py    # System resource monitoring
├── performance_tests/
│   ├── locustfile.py         # Main Locust test file
│   └── test_scenarios.py     # Test behavior definitions
├── reporting/
│   └── report_generator.py   # Custom report generation
├── reports/                  # Generated test reports directory
├── requirements.txt         # Project dependencies
└── README.md               # Project documentation
```

## Features

### Current Implementation
- **Load Testing**: Configurable number of users and spawn rates
- **Custom Reporting**
  - Response time graphs
  - Requests per second visualization
  - Detailed summary reports
- **Resource Monitoring**
  - CPU usage tracking
  - Memory consumption
  - Network I/O metrics
- **Mock Server**
  - FastAPI-based test endpoints
  - Configurable response times
  - Simulated error scenarios
- **Multiple Test Scenarios**
  - Browsing behavior
  - Shopping behavior
  - User profile interactions

## Prerequisites
- Python 3.8+
- pip (Python package installer)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd perf-testing-tool
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the mock server:
```bash
uvicorn mock_server.app:app --reload
```

2. Start resource monitoring (optional):
```bash
python -m monitoring.resource_monitor
```

3. Run performance tests:
```bash
locust -f performance_tests/locustfile.py
```

4. Access the interfaces:
- Locust Web UI: http://localhost:8089
- Mock Server API: http://localhost:8000

## Test Scenarios

### Available Test Types
1. **Smoke Test**
   - Light load for basic verification
   - 5 users, 1 user per second spawn rate

2. **Load Test**
   - Moderate load for performance testing
   - 50 users, 10 users per second spawn rate

3. **Stress Test**
   - Heavy load for system limits testing
   - 100 users, 20 users per second spawn rate

### Endpoints Tested
- GET /api/products
- GET /api/users/{id}
- POST /api/orders

## Reports

Reports are generated in the `reports` directory and include:
- Response time graphs (PNG)
- RPS (Requests Per Second) visualizations (PNG)
- Detailed test summaries (TXT)
- Resource usage statistics (CSV)

## Troubleshooting

Common Issues:
1. **Port Conflicts**
   - Ensure ports 8000 (Mock Server) and 8089 (Locust) are available
   - Change ports using command line arguments if needed

2. **Import Errors**
   - Verify virtual environment is activated
   - Confirm all dependencies are installed: `pip install -r requirements.txt`

3. **Resource Monitoring Issues**
   - Check permissions for system metrics access
   - Verify psutil installation

## Next Steps

1. **Custom Configuration System** (In Progress)
   - YAML-based test scenarios
   - Environment-specific settings
   - Customizable thresholds
   - Test parameter configuration

2. **Planned Enhancements**
   - CI/CD integration
   - Advanced reporting features
   - More test scenarios
   - Additional monitoring capabilities


## License
This is a portfolio project created for educational purposes.
Feel free to use, modify and learn from it.

---

Made with ❤️ by Attila