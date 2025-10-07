import sys
import os
from prefect import flow, task
from datetime import datetime, timedelta

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.fetch_data import fetch_openf1_data
import subprocess

@task
def fetch_data_task():
    """Fetches F1 telemetry data and returns the filename."""
    filename = fetch_openf1_data()
    return filename

@task
def create_duckdb_and_load_data(filename: str):
    """Creates a DuckDB database and loads data from the fetched JSON file."""
    json_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', filename))
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dbt_project', 'f1_telemetry.duckdb'))
    command = f"duckdb {db_path} -c \"CREATE TABLE laps AS SELECT * FROM read_json_auto('{json_file_path}');\""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"DuckDB command failed: {result.stderr}")
    print(result.stdout)

@task
def run_dbt_build_task():
    """Runs dbt build command."""
    dbt_project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dbt_project'))
    command = f"dbt build --project-dir {dbt_project_path}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"dbt build failed: {result.stderr}")
    print(result.stdout)

@flow(name="f1-telemetry-ingestion-flow")
def f1_telemetry_ingestion_flow():
    """
    A Prefect flow to fetch and transform F1 telemetry data using dbt.
    """
    filename = fetch_data_task()
    create_duckdb_and_load_data(filename=filename)
    run_dbt_build_task()

if __name__ == "__main__":
    f1_telemetry_ingestion_flow()
