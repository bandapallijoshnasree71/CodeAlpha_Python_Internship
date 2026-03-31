def simple_chatbot():
    print("Chatbot: Hello! I am a simple rule-based chatbot. Type 'bye' to exit.")
    
    while True:
        # Get user input and convert to lowercase for easy matching
        user_input = input("You: ").lower().strip()

        # Rule-based responses
        if user_input == "hello" or user_input == "hi":
            print("Chatbot: Hi there! How can I help you today?")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a collection of Python rules, but I'm functioning perfectly! How about you?")
            
        elif "your name" in user_input:
            print("Chatbot: I am the CodeAlpha Task 4 Chatbot.")

        elif "python" in user_input:
            print("Chatbot: Python is an amazing language! Are you enjoying your internship?")

        elif user_input == "bye" or user_input == "goodbye":
            print("Chatbot: Goodbye! It was nice talking to you.")
            break # Exit the loop
        
        else:
            print("Chatbot: I'm sorry, I don't understand that yet. Can you try saying 'hello' or 'how are you'?")

if __name__ == "__main__":
    simple_chatbot()
