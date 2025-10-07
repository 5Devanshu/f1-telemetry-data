output "bucket_names" {
  description = "List of all created MinIO buckets"
  value       = [for b in minio_s3_bucket.f1_buckets : b.bucket]
}
