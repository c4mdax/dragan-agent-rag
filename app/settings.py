from pathlib import Path

# Vector basis: ChromaDB
VECTORDB_PATH = Path("./chroma_db")

# Embedding Model: Hugging Face all-MiniLM-L6-v2
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# LLM: Phi3 Mini
LLM_CONFIG = {
    "model": "phi3:mini",  # o "llama3:8b"
    "temperature": 0.3,
    "num_ctx": 4096
}

# RAG Config
CHUNK_SIZE = 300
CHUNK_OVERLAP = 50 
SCORE_THRESHOLD = 0.3  # relevance filter
TOP_K = 3  # relevant fragments to find
