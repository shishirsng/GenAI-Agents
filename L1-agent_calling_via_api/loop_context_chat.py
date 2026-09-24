import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables like OPENAI_API_KEY into environment

from langchain_openrouter import ChatOpenRouter

llm = ChatOpenRouter(
    model="auto")

history = []
while True:
    query = input("User: ")
    history.append({"role": "user", "content": query})
    if query.lower() in ["exit", "quit"]:
        print("AI: Exiting...")
        break
    res = llm.invoke(history)
    print(f"AI: {res.content}")
    history.append({"role": "assistant", "content": res.content})