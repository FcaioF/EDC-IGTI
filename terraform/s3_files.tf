#upload de arquivo contido em pasta local
resource "aws_s3_bucket_object" "codigo_prova" {
    bucket = aws_s3_bucket.datalake_dev.id
    key = "prova-igti/spark/pratico_analise_enem2020.ipynb"
    acl = "private"
    source = "/mnt/48447c52-52ac-4abb-be1b-d26a64732ee0/Documents/cursos/XP_Educação/engenheiro_de_dados_cloud/Modulo1/trabalho_pratico/pratico_analise_enem2020.ipynb"
    etag = filemd5("/mnt/48447c52-52ac-4abb-be1b-d26a64732ee0/Documents/cursos/XP_Educação/engenheiro_de_dados_cloud/Modulo1/trabalho_pratico/pratico_analise_enem2020.ipynb")
}