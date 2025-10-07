variable "minio_server" {
  description = "MinIO server endpoint"
  default     = "localhost:9000"
}

variable "minio_user" {
  description = "MinIO access key"
  default     = "minioadmin"
}

variable "minio_password" {
  description = "MinIO secret key"
  default     = "minioadmin"
}

variable "minio_region" {
  description = "MinIO region"
  default     = "us-east-1"
}

variable "f1_buckets" {
  description = "List of MinIO buckets to create"
  default     = [
    "f1-telemetry-raw",
    "f1-telemetry-transformed",
    "f1-telemetry-analytics"
  ]
}
