from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def retrieve_chunks(questions,index,chunks):
    question_embedding = model.encode(questions)
    question_embedding = np.array(question_embedding).astype('float32')
    question_embedding = question_embedding.reshape(1, -1)
    distances,indices = index.search(question_embedding,3)
    top_chunks = [chunks[i] for i in indices[0]]
    return top_chunks