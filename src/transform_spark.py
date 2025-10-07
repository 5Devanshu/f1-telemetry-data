from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark session with S3A configurations
spark = SparkSession.builder \
    .appName("F1TelemetryTransform") \
    .config("spark.jars.packages",
            "org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.262") \
    .config("spark.hadoop.fs.s3a.access.key", "minioadmin") \
    .config("spark.hadoop.fs.s3a.secret.key", "minioadmin") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://localhost:9001") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
    .config("spark.hadoop.fs.s3a.connection.timeout", "60000") \
    .config("spark.hadoop.fs.s3a.connection.establish.timeout", "60000") \
    .config("spark.hadoop.fs.s3a.attempts.maximum", "3") \
    .config("spark.hadoop.fs.s3a.connection.maximum", "100") \
    .config("spark.hadoop.fs.s3a.threads.max", "10") \
    .config("spark.hadoop.fs.s3a.threads.core", "5") \
    .config("spark.hadoop.fs.s3a.max.total.tasks", "10") \
    .config("spark.hadoop.fs.s3a.multipart.size", "104857600") \
    .getOrCreate()

try:
    # Read JSON data from S3
    df = spark.read.json("s3a://f1-telemetry-raw/raw/f1/laps_20251006_193407.json")
    
    # Check if dataframe is not empty
    if df.count() == 0:
        print("Warning: No data found in source bucket")
    else:
        # Display schema to verify column names
        print("Source data schema:")
        df.printSchema()
        
        # Select and transform columns
        df_transformed = df.select(
            col("driver_number"),
            col("lap_number"),
            col("time"),
            col("sector1_time"),
            col("sector2_time"),
            col("sector3_time")
        )
        
        # Write to S3 as Parquet
        df_transformed.write \
            .mode("overwrite") \
            .parquet("s3a://f1-telemetry-transformed/f1/")
        
        print(f"Successfully transformed {df_transformed.count()} records")

except Exception as e:
    print(f"Error during transformation: {str(e)}")
    raise

finally:
    spark.stop()
