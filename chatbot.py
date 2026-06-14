import json
import random
from datetime import datetime

# Load knowledge base
with open("knowledge_base.json", "r") as file:
    knowledge = json.load(file)

# Intent responses
greetings = [
    "Hello!",
    "Hi there!",
    "Hey!"
]

help_responses = [
    "I can answer questions about Python, AI, Machine Learning and Chatbots.",
    "Try asking me about Python or AI."
]

small_talk = {
    "how are you": "I'm doing well. Thanks for asking!",
    "what is your name": "I am a Rule-Based Chatbot.",
    "who created you": "I was created using Python."
}

print("=== Rule Based Chatbot ===")
print("Type 'bye' to exit.")

while True:

    user_input = input("\nYou: ").lower()

    # Exit
    if user_input == "bye":
        response = "Goodbye!"
        print("Bot:", response)

        with open("chat_history.txt", "a") as log:
            log.write(
                f"{datetime.now()} | User: {user_input} | Bot: {response}\n"
            )
        break

    # Greeting Intent
    elif any(word in user_input for word in ["hello", "hi", "hey"]):
        response = random.choice(greetings)

    # Help Intent
    elif "help" in user_input:
        response = random.choice(help_responses)

    # Small Talk
    elif user_input in small_talk:
        response = small_talk[user_input]

    # Knowledge Base Search
    else:
        response = None

        for key in knowledge:
            if key in user_input:
                response = knowledge[key]
                break

        if response is None:
            response = "Sorry, I don't know the answer to that."

    print("Bot:", response)

    # Log conversation
    with open("chat_history.txt", "a") as log:
        log.write(
            f"{datetime.now()} | User: {user_input} | Bot: {response}\n"
        )