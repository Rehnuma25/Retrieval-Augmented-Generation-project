from rag_pipeline import answer_question

print("RAG Document Q&A System")
print("Type 'exit' to quit\n")

while True:
    q = input("Question: ")
    if q.lower() == "exit":
        break

    ans = answer_question(q)
    print("\n Answer:")
    print(ans)
    print("-" * 50)
