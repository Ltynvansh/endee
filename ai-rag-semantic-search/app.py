from search import search

print("AI Semantic Search System")

while True:
    query = input("\nAsk a question: ")

    if query.lower() == "exit":
        break

    result = search(query)

    print("\nResult:")
    print(result)
