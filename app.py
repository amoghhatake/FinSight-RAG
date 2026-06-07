import streamlit as st
from ingest import ingest_pdf
from retriever import retrieve_chunks
from llm import generate_answer

st.title('FinSight RAG')
uploaded_file = st.file_uploader('Upload a PDF file',type = 'pdf')
question = st.text_input('Ask your question')

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())
    index,chunks = ingest_pdf('temp.pdf')
    st.session_state["index"] = index
    st.session_state["chunks"] = chunks
    st.success('File uploading successful')

if st.button("Ask"):
    index = st.session_state["index"]
    chunks = st.session_state["chunks"]
    top_chunks = retrieve_chunks(question,index,chunks)
    answer = generate_answer(question,top_chunks)
    st.write(answer)