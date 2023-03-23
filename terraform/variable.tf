variable "project" {
  type    = string
  default = "mc-server-381513"
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
  default = "n1-standard-1"
}

variable "network_tags" {
  type    = list(string)
  default = ["minecraft"]
}