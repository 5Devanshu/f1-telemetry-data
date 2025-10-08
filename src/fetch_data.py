import requests
import json
import os
from datetime import datetime
from src.utils.minio_client import upload_to_minio

def fetch_openf1_data():
    url = "https://api.openf1.org/v1/laps"
    params = {"session_key": "latest", "driver_number": "1"}  # example driver
    response = requests.get(url, params=params)
    data = response.json()

    # Ensure 'data' directory exists
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)

    # Save locally
    file_name = os.path.join(data_dir, f"laps_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    with open(file_name, "w") as f:
        json.dump(data, f, indent=2)

    # Upload to MinIO bucket: f1-telemetry-raw
    upload_to_minio(file_name, bucket_name="f1-telemetry-raw", prefix="raw/f1/")

    print(f"✅ Data saved locally and uploaded to MinIO bucket 'f1-telemetry-raw': {file_name}")
    return file_name

if __name__ == "__main__":
    # When run directly, it will just fetch and upload, not return anything to Airflow.
    fetch_openf1_data()
