import psutil
import time
from datetime import datetime
import csv

class ResourceMonitor:
    def __init__(self, output_file="resource_usage.csv"):
        self.output_file = output_file
        self.running = False
        
    def start_monitoring(self):
        self.running = True
        with open(self.output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['timestamp', 'cpu_percent', 'memory_percent', 'network_bytes_sent', 'network_bytes_recv'])
            
            while self.running:
                cpu = psutil.cpu_percent(interval=1)
                memory = psutil.virtual_memory().percent
                network = psutil.net_io_counters()
                
                writer.writerow([
                    datetime.now().isoformat(),
                    cpu,
                    memory,
                    network.bytes_sent,
                    network.bytes_recv
                ])
                time.sleep(1)
    
    def stop_monitoring(self):
        self.running = False