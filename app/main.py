from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from app.claude_service import generate_automation
from config import settings
from pathlib import Path

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    index_path = Path("static/index.html")
    if index_path.exists():
        return index_path.read_text()
    return HTMLResponse(content="<h1>Landing no encontrada</h1>", status_code=404)

@app.post("/automate")
async def automate(request: Request):
    data = await request.json()
    instruction = data.get("instruction")

    if not instruction:
        return JSONResponse({"error": "Falta la instrucción"}, status_code=400)

    try:
        automation = await generate_automation(instruction)
        return JSONResponse(content={"automation": automation})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

