from sentence_transformers import SentenceTransformer

class EmbeddingEngine:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EmbeddingEngine, cls).__new__(cls)
            # Utilizing a free open-source transformer model locally
            cls._instance.model = SentenceTransformer('all-MiniLM-L6-v2')
        return cls._instance

    def embed_text(self, text: str) -> list:
        """Generates raw vector embeddings for a given string."""
        return self.model.encode(text).tolist()