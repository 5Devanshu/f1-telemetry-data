import dask.dataframe as dd
import s3fs
import os
import json # Import the json module
import pandas as pd # Import pandas

# MinIO/S3 configuration
S3_ENDPOINT = os.getenv("S3_ENDPOINT", "http://localhost:9000")
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY", "minioadmin")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY", "minioadmin")
S3_RAW_BUCKET = os.getenv("S3_RAW_BUCKET", "f1-telemetry-raw")
S3_TRANSFORMED_BUCKET = os.getenv("S3_TRANSFORMED_BUCKET", "f1-telemetry-transformed")
S3_RAW_PATH = f"s3://{S3_RAW_BUCKET}/raw/f1/laps_20251006_193407.json" # Example file, will need to be dynamic
S3_TRANSFORMED_PATH = f"s3://{S3_TRANSFORMED_BUCKET}/f1/"

# Configure s3fs for MinIO
fs = s3fs.S3FileSystem(
    key=S3_ACCESS_KEY,
    secret=S3_SECRET_KEY,
    client_kwargs={
        'endpoint_url': S3_ENDPOINT,
    },
    use_ssl=False,
    anon=False
)

def transform_f1_telemetry_data(input_path: str, output_path: str):
    """
    Reads F1 telemetry data from a specified S3 path, transforms it using Dask,
    and writes the transformed data to another S3 path in Parquet format.
    """
    try:
        print(f"Reading data from: {input_path}")
        
        # Read JSON data from S3 using s3fs and parse with json module
        with fs.open(input_path, 'rb') as f:
            json_data = json.loads(f.read().decode('utf-8'))
        
        # Convert to Dask DataFrame from pandas DataFrame
        pandas_df = pd.DataFrame(json_data)
        df = dd.from_pandas(pandas_df, npartitions=1) # npartitions=1 as we read the whole file

        # Check if dataframe is not empty
        if df.npartitions == 0 or df.head(1).empty: # Check if there's any data
            print("Warning: No data found in source bucket or input path.")
            return

        # Select and transform columns
        df_transformed = df[[
            "driver_number",
            "lap_number",
            "lap_duration", # Corrected from "time"
            "duration_sector_1", # Corrected from "sector1_time"
            "duration_sector_2", # Corrected from "sector2_time"
            "duration_sector_3" # Corrected from "sector3_time"
        ]]

        print("Writing transformed data to S3 as Parquet...")
        # Write to S3 as Parquet
        # Dask handles writing multiple partitions to a directory
        df_transformed.to_parquet(output_path,
                                  engine='pyarrow',
                                  overwrite=True,
                                  storage_options={
                                      'key': S3_ACCESS_KEY,
                                      'secret': S3_SECRET_KEY,
                                      'client_kwargs': {
                                          'endpoint_url': S3_ENDPOINT,
                                      },
                                      'use_ssl': False,
                                      'anon': False
                                  })

        print(f"Successfully transformed and wrote data to {output_path}")

    except Exception as e:
        print(f"Error during Dask transformation: {str(e)}")
        raise

if __name__ == "__main__":
    # Example usage:
    # In a real scenario, input_path would be dynamically generated (e.g., from Airflow)
    # For testing, ensure a file like 'laps_20251006_193407.json' exists in your MinIO raw bucket.
    # You might need to adjust the input_path to match an existing file for local testing.
    
    # For demonstration, let's use the same example file as in the Spark script
    # In a real DAG, this would be passed dynamically.
    example_input_file = "laps_20251006_193407.json" 
    dynamic_input_path = f"s3://{S3_RAW_BUCKET}/raw/f1/{example_input_file}"
    
    transform_f1_telemetry_data(dynamic_input_path, S3_TRANSFORMED_PATH)
