import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
VECTOR_STORE_DIR = "./chroma_db"

def get_answer(question):
    # استخدام الطريقة المباشرة للبحث والرد
    vector_store = Chroma(persist_directory=VECTOR_STORE_DIR, embedding_function=embeddings)
    llm = ChatGroq(model_name="llama-3.1-8b-instant", groq_api_key=os.getenv("GROQ_API_KEY"))
    
    # بحث بسيط
    docs = vector_store.similarity_search(question, k=3)
    context = "\n".join([doc.page_content for doc in docs])
    
    # رد الموديل
    response = llm.invoke(f"Context: {context}\n\nQuestion: {question}")
    return response.content