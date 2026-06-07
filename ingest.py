import numpy as np
import fitz
import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_text(pdf_path):
    pdf = fitz.open(pdf_path)
    text = ""
    for page in pdf:
        text += page.get_text()
    return text      

def chunk_text(text, chunk_size):
    chunks = []
    for split in range(0, len(text), chunk_size):
        chunks.append(text[split:split+chunk_size])
    return chunks

def get_embeddings(chunks):
    embeddings = model.encode(chunks)
    return embeddings

def store_in_faiss(embeddings):
    embeddings = np.array(embeddings).astype('float32')
    index = faiss.IndexFlatL2(384)
    index.add(embeddings)
    return index

def ingest_pdf(pdf_path):
    text = extract_text(pdf_path)
    chunks = chunk_text(text,500)
    embeddings = get_embeddings(chunks)
    index = store_in_faiss(embeddings)
    return index,chunks

index, chunks = ingest_pdf("Cover Letter Goldman Sachs.pdf")
