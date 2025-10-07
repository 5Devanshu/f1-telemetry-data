terraform {
  required_providers {
    minio = {
      source  = "aminueza/minio"
      version = ">= 3.0.0"
    }
  }
}

provider "minio" {
  minio_server   = var.minio_server
  minio_user     = var.minio_user
  minio_password = var.minio_password
  minio_region   = var.minio_region
}

# Create buckets from variable list
resource "minio_s3_bucket" "f1_buckets" {
  for_each       = toset(var.f1_buckets)
  bucket         = each.value
  acl            = "private"
  object_locking = false
}
