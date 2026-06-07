from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import shutil
import os
from ingest import ingest_pdf
from retriever import retrieve_chunks
from llm import generate_answer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

store = {
    "index": None,
    "chunks": None
}

class Question(BaseModel):
    question: str

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    with open("temp.pdf", "wb") as f:
        shutil.copyfileobj(file.file, f)
    index,chunks = ingest_pdf("temp.pdf")
    
    store['index'] = index
    store['chunks'] = chunks

    return {"message": "PDF uploaded successfully"}

@app.post("/ask")
async def ask_question(body: Question):
    top_chunks = retrieve_chunks(body.question,store['index'],store['chunks'])
    answer = generate_answer(body.question,top_chunks)
    return {"answer":answer}