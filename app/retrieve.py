from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from config import *

def get_retriever():
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    db = FAISS.load_local(VECTOR_STORE_PATH, embeddings, allow_dangerous_deserialization=True)
    return db.as_retriever(search_kwargs={"k": TOP_K})

def retrieve_docs(query):
    retriever = get_retriever()
    return retriever.invoke(query)