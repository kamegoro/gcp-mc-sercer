provider "google" {
  credentials = file("./../mc-server-terraform_serviceaccount_credential.json")
  project = var.project
  region  = var.region
}