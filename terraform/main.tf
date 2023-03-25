provider "google" {
  credentials = file("${path.module}/mc-server-terraform_serviceaccount_credential.json")
  project = "mc-server-381513"
  region  = var.region
}