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

client_info = []

app.mount("/public/static", StaticFiles(directory="public/static"), name="static")

templates = Jinja2Templates(directory="public/templates")

@app.get("/{number}", response_class=HTMLResponse)
async def read_root(name : str ,request: Request):
    if ({name : request.headers.get('X-Forwarded-For')} in client_info ):
        pass
    else:
        client_info.append({name : request.headers.get('X-Forwarded-For')})
    return templates.TemplateResponse("game.html", {"request": request})

if __name__ == '__main__':
    uvicorn.run(app='main:app',
                host="0.0.0.0",
                port=8000,
                reload=True,
                workers=10)



