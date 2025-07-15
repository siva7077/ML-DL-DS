step1 :  do , touch .env then OPENAI_API_KEY=your_openai_api_key
step 2 : pip install -r requirements.txt
step3 : streamlit run app/streamlit_app.py


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

## 📸 Screenshot

*(Add a screenshot here of the app in action)*

---

## 🧠 Future Ideas

- Add multi-file support
- Allow feedback rating
- Enable local embedding (BGE/MiniLM + HuggingFace)
