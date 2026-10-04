import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from config import *

def load_documents():
    docs = []
    for file in os.listdir(DATA_PATH):
        path = os.path.join(DATA_PATH, file)
        if file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                docs.append(f.read())
    return docs

def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return splitter.create_documents(documents)

def create_vector_store(chunks):
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(VECTOR_STORE_PATH)

if __name__ == "__main__":
    print("Loading documents...")
    docs = load_documents()

    print("Splitting documents...")
    chunks = split_documents(docs)

    print("Creating vector store...")
    create_vector_store(chunks)

    print("Ingestion complete!")

    