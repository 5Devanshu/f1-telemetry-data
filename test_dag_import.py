import os
import sys

# Add the project root to sys.path
project_root = "/Users/devanshu/Desktop/f1-telemetry-project"
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    from airflow.dags.f1_ingestion_dag import dag
    print("DAG imported successfully!")
except ImportError as e:
    print(f"ImportError: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
