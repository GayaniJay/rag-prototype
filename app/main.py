from retrieve import retrieve_docs
from generate import generate_answer

def main():
    print("RAG system ready. Type 'exit' to quit.\n")

    while True:
        query = input("Ask: ")

        if query.lower() == "exit":
            break

        docs = retrieve_docs(query)
        answer = generate_answer(query, docs)

        print("\nAnswer:\n", answer)
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()