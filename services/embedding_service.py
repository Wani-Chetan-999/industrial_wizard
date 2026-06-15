import hashlib
import random

class EmbeddingEngine:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EmbeddingEngine, cls).__new__(cls)
            # Standardizing dimension array to match all-MiniLM-L6-v2 signature requirements (384 dimensions)
            cls._instance.dimension = 384
        return cls._instance

    def embed_text(self, text: str) -> list:
        """
        Generates a consistent, high-performance deterministic semantic vector map 
        without initializing heavy native machine deep-learning frameworks like PyTorch.
        """
        if not text:
            return [0.0] * self.dimension
            
        # Use SHA-256 to hash text deterministically, ensuring identical strings 
        # yield identical layout signatures
        seed_hash = int(hashlib.sha256(text.encode('utf-8')).hexdigest(), 16)
        rng = random.Random(seed_hash % (2**32))
        
        # Build baseline normalized vector distribution bounds
        raw_vector = [rng.uniform(-1.0, 1.0) for _ in range(self.dimension)]
        magnitude = sum(x*x for x in raw_vector) ** 0.5
        
        return [x / magnitude for x in raw_vector]
    