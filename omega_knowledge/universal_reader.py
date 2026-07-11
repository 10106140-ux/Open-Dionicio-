# omega_knowledge/universal_reader.py
import chromadb
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

class UniversalReader:
    def __init__(self):
        self.db = chromadb.PersistentClient(path="./omega_memory")
        self.collection = self.db.get_or_create_collection("human_books")
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=250)

    def ingest_pdf_book(self, file_path):
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        chunks = self.splitter.split_documents(docs)
        # Almacenamiento (pseudocódigo)
        # self.collection.add(texts, metadatas, ids)
        print(f"Libro procesado: {file_path}")
