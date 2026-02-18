SYSTEM_PROMPT = """
You are a helpful AI assistant.
Answer ONLY from the provided context.
If the answer is not in the context, say "I don't know".
"""

def build_prompt(context, question):
    return f"""
Context:
{context}

Question:
{question}

Answer:
"""
