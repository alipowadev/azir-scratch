# A bucket for exported reports (P15 integration test: an infra/ change always needs an admin).
resource "google_storage_bucket" "reports" {
  name                        = "azir-scratch-reports"
  location                    = "EU"
  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"

  lifecycle_rule {
    condition {
      age = 30
    }
    action {
      type = "Delete"
    }
  }
}
