import os
import openai
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY environment variable not set")

openai.api_key = OPENAI_API_KEY


def chat_with_gpt(prompt: str, model: str = "gpt-3.5-turbo") -> str:
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


def main():
    print("Welcome to the AI Chatbot!")
    while True:
        try:
            user_input = input("You: ")
        except EOFError:
            break
        if user_input.lower() in {"exit", "quit"}:
            break
        reply = chat_with_gpt(user_input)
        print(f"Bot: {reply}")


if __name__ == "__main__":
    main()
