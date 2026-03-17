variable "region" {
  default = "aws"
}
variable "zone" {
  default = "ap-southeast-1a"
}
variable "amiID" {
  type = map
  default = {
    ap-southeast-1a = "ami-00d8fc944fb171e29"
    ap-southeast-1b = "ami-0f5fcdfbd140e4ab7"
  }
}
variable "user" {
  default = "ubuntu"
}