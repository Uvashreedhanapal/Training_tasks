
provider "google" {
  credentials = file("C:\\Users\\HI\\Downloads\\uvashree-407406-e7880a36fb4e.json")
  project     = "uvashree-407406"
  region      = "us-central1"
}

# 4 Try static and dynamic values passing for the variables that will be used by the resource during creationtime.
variable "bucket_name" {
  type    = string
  default = "uvash_bucket"
}

# 4
variable "bucket_location" {
  type    = string
  default = "US"
}

# 1 Create any one resource using terraform in any cloud.
resource "google_storage_bucket" "my_bucket" {
  name     = var.bucket_name
  location = var.bucket_location
}
  
# 2 Try local and cloud storage backend configuration to store state files.
# 3 Try to use depends on module in code.
data "terraform_remote_state" "store" {
  depends_on = [google_storage_bucket.my_bucket]

  backend = "gcs"

  config = {
    bucket  = "uvash_bucket"
    prefix  = "statefile"
  }
}

#5. Print the output of a resource which you have created.

output "bucket_url" {
  value = google_storage_bucket.my_bucket.url
}
