import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import os
import logging

class PerformanceReportGenerator:
    def __init__(self):
        self.report_dir = "reports"
        self.ensure_report_directory()
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
    
    def ensure_report_directory(self):
        if not os.path.exists(self.report_dir):
            os.makedirs(self.report_dir)
            self.logger.info(f"Created reports directory: {self.report_dir}")
    
    def generate_report(self, stats):
        self.logger.info("Starting report generation...")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Convert stats to DataFrame
        data = []
        self.logger.info(f"Processing {len(stats.entries)} stat entries")
        
        # Process stats entries correctly
        for endpoint, entry in stats.entries.items():
            # Convert tuple endpoint to string
            endpoint_name = endpoint[0] if isinstance(endpoint, tuple) else str(endpoint)
            self.logger.info(f"Processing endpoint: {endpoint_name}")
            
            data.append({
                'Name': endpoint_name,
                'Requests': entry.num_requests,
                'Failures': entry.num_failures,
                'Median': entry.median_response_time,
                'Average': entry.avg_response_time,
                'RPS': entry.current_rps
            })
        
        if not data:
            self.logger.warning("No data to process!")
            return
        
        df = pd.DataFrame(data)
        self.logger.info(f"Created DataFrame with {len(df)} rows")
        
        try:
            # Generate plots
            self.plot_response_times(df, timestamp)
            self.plot_requests_per_second(df, timestamp)
            self.generate_summary(df, timestamp)
            self.logger.info("Report generation completed successfully")
        except Exception as e:
            self.logger.error(f"Error generating report: {str(e)}")
            raise
    
    def plot_response_times(self, df, timestamp):
        self.logger.info("Generating response times plot...")
        plt.figure(figsize=(10, 6))
        
        # Create bar plot
        x = range(len(df['Name']))
        plt.bar(x, df['Median'], label='Median', width=0.35)
        plt.bar(x, df['Average'], alpha=0.5, label='Average', width=0.35)
        
        # Customize plot
        plt.title('Response Times by Endpoint')
        plt.xlabel('Endpoint')
        plt.ylabel('Response Time (ms)')
        plt.xticks(x, df['Name'], rotation=45, ha='right')
        plt.legend()
        
        plt.tight_layout()
        output_path = f"{self.report_dir}/response_times_{timestamp}.png"
        plt.savefig(output_path)
        plt.close()
        self.logger.info(f"Saved response times plot to {output_path}")
    
    def plot_requests_per_second(self, df, timestamp):
        self.logger.info("Generating RPS plot...")
        plt.figure(figsize=(10, 6))
        
        # Create bar plot
        x = range(len(df['Name']))
        plt.bar(x, df['RPS'])
        
        # Customize plot
        plt.title('Requests per Second by Endpoint')
        plt.xlabel('Endpoint')
        plt.ylabel('Requests/s')
        plt.xticks(x, df['Name'], rotation=45, ha='right')
        
        plt.tight_layout()
        output_path = f"{self.report_dir}/rps_{timestamp}.png"
        plt.savefig(output_path)
        plt.close()
        self.logger.info(f"Saved RPS plot to {output_path}")
    
    def generate_summary(self, df, timestamp):
        self.logger.info("Generating summary report...")
        output_path = f"{self.report_dir}/summary_{timestamp}.txt"
        with open(output_path, 'w') as f:
            f.write("Performance Test Summary\n")
            f.write("=======================\n\n")
            f.write(f"Total Requests: {df['Requests'].sum()}\n")
            f.write(f"Total Failures: {df['Failures'].sum()}\n")
            f.write(f"Average Response Time: {df['Average'].mean():.2f}ms\n")
            f.write(f"Average RPS: {df['RPS'].mean():.2f}\n")
            
            # Add per-endpoint details
            f.write("\nPer-Endpoint Details:\n")
            f.write("-------------------\n")
            for _, row in df.iterrows():
                f.write(f"\nEndpoint: {row['Name']}\n")
                f.write(f"  Requests: {row['Requests']}\n")
                f.write(f"  Failures: {row['Failures']}\n")
                f.write(f"  Average Response Time: {row['Average']:.2f}ms\n")
                f.write(f"  RPS: {row['RPS']:.2f}\n")
                
        self.logger.info(f"Saved summary to {output_path}")