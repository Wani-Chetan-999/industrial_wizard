import os
import fitz  # PyMuPDF
import chromadb
from django.conf import settings
from services.embedding_service import EmbeddingEngine
from langchain.text_splitter import RecursiveCharacterTextSplitter

class RagKnowledgeEngine:
    def __init__(self):
        self.db_dir = os.getenv("CHROMA_DB_DIR", "./chroma_db")
        self.chroma_client = chromadb.PersistentClient(path=self.db_dir)
        self.embedding_engine = EmbeddingEngine()
        
        # Explicitly pass a baseline dummy function since we handle token mapping manually
        self.collection = self.chroma_client.get_or_create_collection(
            name="steel_plant_sops",
            embedding_function=lambda x: [[]]  
        )
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=100)

    def process_and_index_pdf(self, file_path: str, document_id: str):
        doc = fitz.open(file_path)
        full_text = ""
        for page in doc:
            full_text += page.get_text()
            
        chunks = self.text_splitter.split_text(full_text)
        
        for index, chunk in enumerate(chunks):
            embedding = self.embedding_engine.embed_text(chunk)
            self.collection.add(
                embeddings=[embedding],
                documents=[chunk],
                metadatas=[{"doc_id": document_id, "chunk_index": index}],
                ids=[f"{document_id}_{index}"]
            )

    def query_knowledge_base(self, query_text: str, n_results: int = 3) -> list:
        query_embedding = self.embedding_engine.embed_text(query_text)
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
        return results['documents'][0] if results['documents'] else []