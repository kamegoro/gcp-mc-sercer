variable "project" {
  type    = string
  default = "smaple"
}

variable "region" {
  type    = string
  default = "asia-northest1"
}

variable "zone" {
  type    = string
  default = "asia-northest1-a"
}

variable "machine_type" {
  type    = string
  default = "n1-standard-1"
}

variable "network_tags" {
  type    = list(string)
  default = ["minecraft"]
}