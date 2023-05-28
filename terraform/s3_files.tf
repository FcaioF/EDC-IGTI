#upload de arquivo contido em pasta local
resource "aws_s3_bucket_object" "codigo_prova" {
    bucket = aws_s3_bucket.datalake_dev.id
    key = "prova-igti/spark/pratico_analise_enem2020.ipynb"
    acl = "private"
    source = "terraform/arquivos_upload/*"
    etag = filemd5("terraform/arquivos_upload/*")
}