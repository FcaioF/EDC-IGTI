provider "aws" {
    region = ("${var.aws_region}")
}

#centralizar o arquivo de controle de estado do terraform
terraform {
  backend "s3" {
    bucket = "terraform-state-igti-caio"
    key = "state/igit/edc/mod1/terraform.tfstate"
    region = "us-east-1"
    
  }
}