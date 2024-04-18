resource "aws_s3_bucket" "bucket" {
  bucket = "mybucket"
  acl    = "public-read"

  website {
    index_document = "index.html"
    error_document = "error.html"
  }
}
