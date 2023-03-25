variable "project" {
  type    = string
  default = "smaple"
}

variable "region" {
  type    = string
  default = "asia-northeast1"
}

variable "zone" {
  type    = string
  default = "asia-northeast1-a"
}

# NOTE: GCPのマシンスペック
variable "machine_type" {
  type    = string
  default = "n2-standard-2"
}

variable "network_tags" {
  type    = list(string)
  default = ["minecraft"]
}