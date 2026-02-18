from langchain_community.llms import Ollama
from .utils import load_vectorstore
from .prompts import SYSTEM_PROMPT

def answer_question(question: str):
    db = load_vectorstore("vectorstore")

    docs = db.similarity_search(question, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])

    llm = Ollama(model="llama3")   # এখানে শুধু llama3 দিলেই হবে

    prompt = f"""
    {SYSTEM_PROMPT}

    Context:
    {context}

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    return response
