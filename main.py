from fastapi import FastAPI,Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import requests
import json
import asyncio
import uvicorn

app = FastAPI()

app.mount("/public/static", StaticFiles(directory="public/static"), name="static")

templates = Jinja2Templates(directory="./public/templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/reservation/{number}")
def send(number: int):
    print(number)
    return f"{number}번 전송 완료"

if __name__ == '__main__':
    uvicorn.run(app='main:app',
                host="0.0.0.0",
                port=8000,
                reload=True,
                workers=10)



