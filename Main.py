from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from app.engine import get_ai_move

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/move")
async def move(request: Request):
    data = await request.json()
    fen = data.get("fen")
    ai_move = get_ai_move(fen)
    return JSONResponse({"ai_move": ai_move})
