# Retrieval-Augmented-Generation-project
# RAG Project – Retrieval-Augmented Generation

A Retrieval-Augmented Generation (RAG) system built using LLM + Vector Database to provide context-aware answers from custom documents.



## Project Overview

This project implements a RAG pipeline that:

1. Loads custom documents
2. Converts them into embeddings
3. Stores them in a vector database
4. Retrieves relevant chunks based on user query
5. Generates a context-aware response using an LLM

---

##  Tech Stack

- Python 3.10+
- LangChain
- HuggingFace LLM
- FAISS (Vector Database)
- FastAPI 

---

##Create virtual environment:
venv\Scripts\activate   

-------
##Ingest Documents:
python ingest.py

This will:

1.Load documents
2.Create embeddings
3.Store in vector database

-------
<img width="539" height="238" alt="Screenshot 2026-02-18 195545" src="https://github.com/user-attachments/assets/e3863ed6-9904-413b-9553-89815c42a315" />
index.html shows:
<img width="1584" height="551" alt="cf1030cc-f576-47e1-9411-e4f46d074121" src="https://github.com/user-attachments/assets/472febad-7aa0-4ec6-800b-632d457b3890" />



