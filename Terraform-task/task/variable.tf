# 4 Try static and dynamic values passing for the variables that will be used by the resource during creationtime.
# static variable
variable "bucket_name" {
  type    = string
  default = "uvash_bucket"
}

# 4 dynamic variable
variable "bucket_location" {
  type    = string
  
}

# for dynamic input need to give value like this:  terraform apply -var="bucket_location=us-central1"