from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from redis import Redis


app = FastAPI()
redis = Redis(host='redis', port=6379)
@app.get('/',response_class=HTMLResponse)
async def root():
    redis.incr("count")
    count = str(redis.get("count"),"utf-8")
    return f"""
    <!DOCTYPE html>
<html>
<head>
  <title>Motos</title>
</head>
<body>
  <h1>Sonhos de consumo</h1>

  <h1>quantidade de visitas ao site: {count}</h1>
  
  <h2>Yamaha Tracer 900GT </h2>
  <img src="https://www.zabikers.co.za/wp-content/uploads/2019/11/Tracer-Cover.jpg" alt="Imagem 1">
  
  <h2>Honda Africa Twin 1100</h2>
  <img src="https://motos2022.pro.br/wp-content/uploads/2022/03/web-IMG_4515.png" alt="Imagem 2">
  
  <h2>Tiger 900 Rally</h2>
  <img src="https://www.webmotors.com.br/wp-content/uploads/2023/03/03172715/Triumph-Tiger-900-Rally-Pro.webp" alt="Imagem 3">
</body>
</html>    
    """
@app.get('/healthz')
async def health():
    return {
        "messagem":"application running correctly"
            }

