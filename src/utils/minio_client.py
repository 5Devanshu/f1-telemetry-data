from minio import Minio
import os

# Initialize MinIO client
client = Minio(
    "localhost:9000",
    access_key=os.getenv("MINIO_ACCESS_KEY", "minioadmin"),
    secret_key=os.getenv("MINIO_SECRET_KEY", "minioadmin"),
    secure=False,  # False for HTTP, True for HTTPS
)

def upload_to_minio(file_path, bucket_name="f1-telemetry", prefix=""):
    """
    Uploads a local file to MinIO.
    
    Args:
        file_path (str): Path to the local file
        bucket_name (str): MinIO bucket name
        prefix (str): Folder prefix inside the bucket (e.g., 'raw/f1/')
    """
    # Create bucket if it doesn't exist
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)
        print(f"📦 Created bucket: {bucket_name}")

    # Ensure prefix ends with '/'
    if prefix and not prefix.endswith('/'):
        prefix += '/'

    # Build object name
    object_name = prefix + os.path.basename(file_path)

    # Upload file
    client.fput_object(bucket_name, object_name, file_path)
    print(f"✅ Uploaded {object_name} to MinIO bucket {bucket_name}")
