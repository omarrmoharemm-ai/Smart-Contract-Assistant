from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os

# استخدام موديل مجاني للـ Embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
VECTOR_STORE_DIR = "./chroma_db"

def process_and_store_document(file_path):
    # 1. قراءة الملف
    loader = PyMuPDFLoader(file_path)
    documents = loader.load()
    
    # 2. [span_0](start_span)[span_1](start_span)تقطيع النص (Chunking)[span_0](end_span)[span_1](end_span)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(documents)
    
    # 3. [span_2](start_span)[span_3](start_span)تخزين في Vector Store[span_2](end_span)[span_3](end_span)
    vector_store = Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        persist_directory=VECTOR_STORE_DIR
    )
    return "تمت معالجة العقد بنجاح وجاهز للدردشة!"