import os
import streamlit as st
from dotenv import load_dotenv
from src.loader import load_and_split
from src.vector_store import create_vector_store
from src.chatbot import create_qa_chain

load_dotenv()

st.set_page_config(page_title="Doc Chatbot", page_icon="📄")
st.title("📄 Chat with Your Document")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    with st.spinner("Reading and indexing..."):
        docs = load_and_split(uploaded_file.name)
        db = create_vector_store(docs)
        qa = create_qa_chain(db)
        st.success("Ready to answer questions!")

    query = st.text_input("Ask a question from the document:")
    if query:
        with st.spinner("Generating answer..."):
            result = qa.run(query)
            st.write(result)
