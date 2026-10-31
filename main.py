"""
CodeAlpha Task 4: Basic Chatbot
A beginner-friendly, rule-based chatbot using functions, loops, and if-elif logic.
"""

def get_response(user_message):
    """Return a predefined response based on the user's message."""
    message = user_message.strip().lower()

    if message in ("hello", "hi", "hey"):
        return "Hi! Nice to meet you. How can I help you?"
    elif message in ("how are you", "how are you?"):
        return "I'm fine, thanks for asking! How are you?"
    elif message in ("i am fine", "i'm fine", "good", "great"):
        return "That's great to hear!"
    elif message in ("what is your name", "what's your name", "your name"):
        return "I'm CodeAlpha Bot, a simple Python chatbot."
    elif message in ("what can you do", "help"):
        return "I can respond to a few basic messages. Try saying hello, asking how I am, or saying bye."
    elif message in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that yet. Please try another message."


def chat():
    """Run the chatbot until the user chooses to exit."""
    print("=" * 48)
    print("             CODEALPHA BASIC CHATBOT")
    print("=" * 48)
    print("Bot: Hello! I'm CodeAlpha Bot.")
    print("Bot: Type 'help' to see what I can respond to.")
    print("Bot: Type 'bye' whenever you want to end the chat.")
    print("-" * 48)

    while True:
        user_message = input("You: ").strip()

        if not user_message:
            print("Bot: Please type a message.")
            continue

        response = get_response(user_message)
        print("Bot:", response)

        if user_message.lower().strip() in ("bye", "goodbye", "exit", "quit"):
            break


if __name__ == "__main__":
    chat()
