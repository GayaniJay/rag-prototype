# RAG Project – Company Policy Q&A

A simple Retrieval-Augmented Generation (RAG) application built for learning and understanding the basic RAG workflow. The system uses a company policy document as its knowledge base, converts the document into vector embeddings, stores them in a FAISS vector database, retrieves the most relevant document chunks for a user's question, and uses an OpenAI LLM to generate an answer based only on the retrieved context.

> Note: This project was created for learning and demonstration purposes. It is a simple RAG implementation and is not intended to be a production-ready enterprise RAG system.

# Features

- Load .txt documents from the knowledge-base directory
- Split documents into smaller chunks
- Generate vector embeddings using OpenAI
- Store embeddings in a FAISS vector database
- Retrieve the most relevant document chunks using vector similarity search
- Generate answers using OpenAI GPT-4.1-mini
- Interactive command-line question-and-answer interface
- Configurable chunk size, overlap, and number of retrieved documents

# File Description

app/config.py : Contains model, RAG, and path configurations
app/ingest.py : Loads documents, splits them into chunks, creates embeddings, and builds the FAISS vector store
app/retrieve.py : Loads the FAISS vector store and retrieves relevant document chunks
app/generate.py : Creates the prompt and generates an answer using the OpenAI LLM
app/main.py : Runs the interactive command-line RAG application
data/documents/company_policy.txt : Sample knowledge-base document
data/vector_store/ : Contains the generated FAISS vector store
.env : Stores the OpenAI API key
requirements.txt : Lists Python dependencies

# Models

EMBEDDING_MODEL = "text-embedding-3-small"
LLM_MODEL = "gpt-4.1-mini"

# Set Up

> Prerequisites : 
    - Python installed
    - OPENAI API key

> Steps :
    - Create a virtual environment : python -m venv .venv
    - Activate virtual environment : .venv\Scripts\activate
    - Install dependencies : pip install -r requirements.txt
    - Configure OpenAI API key : Update the OpenAI key in the given .env file in the project root : OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
    
    - Create vectore store : At the first run or only if you do any changes to knowledge base please run : python app/ingest.py
    - Run the RAG application : python app/main.py 
    - Exit the RAG application : exit

> Example test questions :
    - How many days of annual leave do employees receive?
    - What are the standard working hours?
    - How much notice is required before resignation?
    - What are the requirements for remote work?
    - How often are employee performance reviews conducted?
    - What security practices are mandatory?
