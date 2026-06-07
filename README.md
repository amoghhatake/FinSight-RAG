# FinSight RAG

A RAG-powered financial document analyst that lets you upload any financial PDF and ask natural language questions about it gets powered by local LLMs via Ollama.

## What it does

Upload a bank statement, annual report, or any financial PDF and ask questions like:

- "What are the key risks mentioned?"
- "What was the net profit this year?"
- "What did the CEO say about growth?"

## How it works

1. PDF is uploaded and text is extracted using PyMuPDF
2. Text is split into chunks of 500 characters
3. Each chunk is converted to embeddings using SentenceTransformers
4. Embeddings are stored in a FAISS vector index
5. User asks a question it gets embedded and compared against all chunks
6. Top 3 most relevant chunks are retrieved from FAISS
7. Chunks + question are sent to Ollama (llama3) to generate a grounded answer

## Tech Stack

- **Backend** : FastAPI
- **Vector DB** : FAISS
- **Embeddings** : SentenceTransformers (all-MiniLM-L6-v2)
- **LLM** : Ollama (llama3)
- **Frontend** : Streamlit
- **PDF Parsing** : PyMuPDF

## How to Run

1. Clone the repo
2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Make sure Ollama is running with llama3 pulled

```bash
ollama run llama3
```

4. Run the app

```bash
cd backend
streamlit run app.py
```

## Project Structure

```
finsight-rag/
├── backend/
│   ├── ingest.py        # PDF → chunks → embeddings → FAISS
│   ├── retriever.py     # question → FAISS search → top chunks
│   ├── llm.py           # chunks + question → Ollama → answer
│   ├── main.py          # FastAPI REST API
│   └── app.py           # Streamlit UI
└── README.md
```
