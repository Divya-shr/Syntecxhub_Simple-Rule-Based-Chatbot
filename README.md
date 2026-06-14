# Simple Rule-Based Chatbot

## Overview

This project is a Simple Rule-Based Chatbot developed using Python. The chatbot uses pattern matching and predefined rules to respond to user queries. It supports greetings, help requests, small talk, and answers domain-specific questions from a knowledge base. The chatbot also logs conversation history for future reference.

---

## Features

* Greeting Intent Recognition
* Help Intent Support
* Small Talk Responses
* Knowledge Base Question Answering
* Interactive Console-Based Chat
* Conversation History Logging
* Simple and Easy-to-Understand Python Implementation

---

## Technologies Used

* Python 3.x
* JSON
* File Handling
* Pattern Matching
* VS Code

---

## Project Structure

```text
SimpleRuleBasedChatbot/
│
├── chatbot.py
├── knowledge_base.json
├── README.md
├── .gitignore
└── chat_history.txt
```

---

## Knowledge Base

The chatbot retrieves answers from a JSON-based knowledge base.

Example:

```json
{
    "python": "Python is a high-level programming language.",
    "ai": "Artificial Intelligence enables machines to simulate human intelligence.",
    "machine learning": "Machine Learning is a subset of AI that learns from data.",
    "chatbot": "A chatbot is a software application that simulates conversation."
}
```

---

## How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/simple-rule-based-chatbot.git
```

### Step 2: Navigate to the Project Directory

```bash
cd simple-rule-based-chatbot
```

### Step 3: Run the Chatbot

```bash
python chatbot.py
```

---

## Sample Interaction

```text
=== Rule Based Chatbot ===
Type 'bye' to exit.

You: hello
Bot: Hi there!

You: what is python
Bot: Python is a high-level programming language.

You: how are you
Bot: I'm doing well. Thanks for asking!

You: bye
Bot: Goodbye!
```

---

## Conversation Logging

All conversations are automatically stored in the `chat_history.txt` file with timestamps.

Example:

```text
2026-06-14 10:15:21 | User: hello | Bot: Hi there!
2026-06-14 10:15:35 | User: what is python | Bot: Python is a high-level programming language.
```

---

## Future Enhancements

* GUI Interface using Tkinter
* Database Integration
* NLP-Based Intent Recognition
* Voice-Based Interaction
* Web-Based Chatbot Deployment

---

## Learning Outcomes

Through this project, the following concepts were explored:

* Rule-Based Conversational Systems
* Pattern Matching Techniques
* Python File Handling
* JSON Data Management
* Interactive Console Applications
* Conversation Logging

---

## Author

Konni Divya

Internship Project – Simple Rule-Based Chatbot

---

## License

This project is created for educational and internship learning purposes.
