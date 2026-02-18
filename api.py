print("API.PY LOADED")

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .rag_pipeline import answer_question

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ask")
async def ask(request: Request, question: str = Form(...)):
    answer = answer_question(question)

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "question": question,
            "answer": answer
        }
    )

