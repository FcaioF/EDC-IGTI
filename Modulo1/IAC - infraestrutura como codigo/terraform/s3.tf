resource "aws_s3_bucket" "datalake_dev" {
  #parametro de configuracao do recurso escolhido
  bucket = ("${var.base_bucket_name}-${var.enviroment}-${var.account_number}")
  acl = "private"

  server_side_encryption_configuration {
    rule {
        apply_server_side_encryption_by_default {
            sse_algorithm = "AES256"
        }
    }
  }
  tags = {
    IES = "IGTI",
    CURSO = "EDC"
  }
    
}