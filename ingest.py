import os
from app.utils import load_documents, split_docs, save_vectorstore

#Project root path (upomallm/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Absolute paths (Windows-safe)
DATA_DIR = os.path.join(BASE_DIR, "data", "docs")
VECTOR_DIR = os.path.join(BASE_DIR, "data", "vectorstore")


def run_ingest():
    all_docs = []

    # safety check
    if not os.path.exists(DATA_DIR):
        print(f"DATA_DIR not found: {DATA_DIR}")
        return

    for file in os.listdir(DATA_DIR):
        if file.lower().endswith(".pdf"):
            file_path = os.path.join(DATA_DIR, file)
            docs = load_documents(file_path)
            all_docs.extend(docs)

    if not all_docs:
        print("⚠️ No documents found in data/docs")
        return

    chunks = split_docs(all_docs)
    save_vectorstore(chunks, VECTOR_DIR)

    print("✅ Documents indexed successfully")


if __name__ == "__main__":
    run_ingest()
