

def chat():
    responses = {
        "hello": "Hello! How can I assist you today?",
        "hi": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm here to help!",
        "what is your name": "I'm a customer support chatbot!",
        "help": "I can help with general inquiries. Please ask your question!",
        "bye": "Goodbye! Have a great day!",
        "services": "We offer a variety of services including customer support, order tracking, and general inquiries.",
    
    }
    
    while True:
        user_message = input("You: ").strip().lower()
        if user_message in responses:
            print("Bot:", responses[user_message])
        else:
            print("Bot: I'm sorry, I don't understand that. Can you please rephrase?")
        
        if user_message == "bye":
            break

if __name__ == "__main__":
    chat()