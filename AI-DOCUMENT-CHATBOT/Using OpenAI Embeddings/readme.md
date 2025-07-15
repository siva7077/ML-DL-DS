

# 📄 AI Chatbot for PDF Documents

An interactive chatbot that lets you upload a PDF and ask questions based on its content.

## 🔍 Features

- Upload and process PDF documents
- Uses OpenAI + FAISS for semantic search
- Powered by LangChain RetrievalQA
- Simple Streamlit frontend

## ⚙️ Tech Stack

- LangChain
- OpenAI GPT & Embeddings
- FAISS (for vector DB)
- Streamlit
- dotenv

## 🚀 Running Locally

1. Clone the repo
2. Create `.env` file with your OpenAI API key
3. Install requirements:  
   `pip install -r requirements.txt`
4. Run the app:  
   `streamlit run app/streamlit_app.py`



## 🧠 Future Ideas

- Add multi-file support
- Allow feedback rating
- Enable local embedding (BGE/MiniLM + HuggingFace)

