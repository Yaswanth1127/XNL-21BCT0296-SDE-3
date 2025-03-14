provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "fintech_server" {
  ami             = "ami-0abcdef1234567890" # Choose a suitable Amazon Linux image
  instance_type   = "t3.medium"
  user_data       = file("startup_script.sh")
  tags = {
    Name = "Fintech Server"
  }
}
