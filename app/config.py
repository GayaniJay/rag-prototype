import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Model configs
EMBEDDING_MODEL = "text-embedding-3-small"
LLM_MODEL = "gpt-4.1-mini"

# RAG configs
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
TOP_K = 3

# Paths
DATA_PATH = "data/documents"
VECTOR_STORE_PATH = "data/vector_store"