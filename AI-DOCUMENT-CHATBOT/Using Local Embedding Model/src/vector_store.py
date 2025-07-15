from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def create_vector_store(docs):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(docs, embeddings)
    return db
