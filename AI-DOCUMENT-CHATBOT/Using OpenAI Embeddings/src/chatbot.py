from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

def create_qa_chain(db):
    return RetrievalQA.from_chain_type(
        llm=OpenAI(temperature=0),
        retriever=db.as_retriever()
    )
