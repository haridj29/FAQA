from knowledge_base import knowledge

print("Simple AI Question Answering System")
print("Type 'exit' to quit\n")

while True:

    question = input("You: ").lower()

    if question == "exit":
        break

    answer = knowledge.get(question)

    if answer:
        print("AI:", answer)
    else:
        print("AI: Sorry, I don't know the answer.")