# CodeAlpha Basic Chatbot

**Task:** CodeAlpha Python Programming – Task 4  
**Project type:** Rule-based console chatbot  
**Language:** Python 3

## Overview

CodeAlpha Bot is a small, text-based chatbot. It reads a message from the user and selects a predefined reply using Python `if-elif-else` conditions. The conversation continues in a loop until the user enters `bye`, `goodbye`, `exit`, or `quit`.

## Features

- Responds to greetings such as `hello`, `hi`, and `hey`.
- Responds to `how are you`.
- Recognizes a few additional predefined messages.
- Displays a helpful response for unknown messages.
- Handles empty input without closing the program.
- Ends the conversation when the user types an exit word.

## Requirements

- Python 3.x
- No external libraries are required.

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python3 main.py
   ```

## Example Conversation

```text
CODEALPHA BASIC CHATBOT
Bot: Hello! I'm CodeAlpha Bot.
You: hello
Bot: Hi! Nice to meet you. How can I help you?
You: how are you
Bot: I'm fine, thanks for asking! How are you?
You: bye
Bot: Goodbye! Have a great day!
```

## Python Concepts Used

- Functions (`get_response()` and `chat()`)
- `while` loop
- `if-elif-else` conditional statements
- String methods (`strip()` and `lower()`)
- Console input and output

## Project Structure

```text
CodeAlpha_BasicChatbot/
├── main.py
├── README.md
└── sample_output.txt
```

## Scope

This is a basic rule-based chatbot created for the CodeAlpha Task 4 requirements. It does not use AI, machine learning, an API, or an internet connection. Its replies are selected from predefined rules.
