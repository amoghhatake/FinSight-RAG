import requests

def generate_answer(question,top_chunks):
    context = '\n\n'.join(top_chunks)
    response = requests.post("http://localhost:11434/api/generate",
    json={
        "model": "llama3",
        "prompt": f"""You are a financial document assistant.
Answer the question based only on the context below.

    Context:
    {context}

    Question:
    {question}""",
        "stream": False
    }
)
    answer = response.json()["response"]
    return answer