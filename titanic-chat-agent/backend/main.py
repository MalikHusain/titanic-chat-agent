from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from agent import run_query
import os

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
def ask_question(request: QueryRequest):
    result = run_query(request.question)

    if isinstance(result, dict):
        return result
    else:
        return {"text": result}


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)        