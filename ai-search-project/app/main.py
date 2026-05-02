from app.index_data import index_pdf
from app.chat import ask_question

if __name__ == "__main__":
    # Step 1: Index PDF (run once)
    # index_pdf("sample.pdf")

    # Step 2: Chat loop
    while True:
        query = input("\nAsk something (or 'exit'): ")

        if query.lower() == "exit":
            break

        answer = ask_question(query)

        print("\n💡 Answer:\n")
        print(answer)
