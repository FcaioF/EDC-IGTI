#imagem do linux que sera usada (alpine ultima versão)
FROM alpine:3.18.2
# aplicações que iremos instalar na imagem (python e pip) comando no-cache usado para deixar aplicacao enxuta
RUN apk add --no-cache python3 py3-pip
#executa comando para instalar as bibliotecas necessarias.
RUN pip install --no-cache-dir fastapi==0.97.0 uvicorn==0.22.0 redis-py-cluster
#expondo a porta padrao do servidor uvicorn
EXPOSE 8000
#copiando todo o conteudo da pasta src para dentro da imagem docker
COPY ./src /app
#apos a instalacao o comando a seguir sera executado para iniciar o servidor uvicorn
CMD ["uvicorn","app.api:app","--host","0.0.0.0"]