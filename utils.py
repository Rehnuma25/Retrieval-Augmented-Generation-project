from langchain_community.document_loaders import PyPDFLoader, UnstructuredPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os


def load_documents(file_path):
    docs = []
    try:
        loader = PyPDFLoader(file_path)
        docs = loader.load()
    except Exception:
        print(" PyPDFLoader failed, using UnstructuredPDFLoader")
        loader = UnstructuredPDFLoader(file_path)
        docs = loader.load()

    # remove empty pages
    docs = [d for d in docs if d.page_content and d.page_content.strip()]
    return docs


def split_docs(docs):
    if not docs:
        return []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(docs)

    # remove empty chunks
    chunks = [c for c in chunks if c.page_content.strip()]
    return chunks


def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )



def save_vectorstore(docs, path):
    if not docs:
        raise ValueError("No valid text chunks found to embed")

    embeddings = get_embeddings()
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(path)


def load_vectorstore(path):
    embeddings = get_embeddings()
    return FAISS.load_local(
        path,
        embeddings,
        allow_dangerous_deserialization=True
    )


