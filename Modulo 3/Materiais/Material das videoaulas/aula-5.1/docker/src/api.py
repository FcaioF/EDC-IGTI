from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
  return """"
      <html>
        <head>
          <title>My FastApi</title>
        </head>

        <body style="background: radial-gradient(circle at 10% 20%, rgb(0, 0, 0) 0%, rgb(64, 64, 64) 90.2%);">
          <div style="text-align: center;line-height: 200px;color: rgb(0, 201, 0);">
            <h1>XP Educação | Aprenda com quem faz</h1>
          </div>
          <div style="text-align: center;line-height: 200px;color: rgb(0, 201, 0);">
            <h1>Versão 2.0.0</h1>
          </div>
        </body>
      </html>  
  """

@app.get("/healthz")
async def health():
  return {
    "message": "ok!"
  }