def get_bot_response(user_input):
    """
    Takes the user's input, converts it to lowercase, 
    and returns the matching chatbot response.
    """
    # Convert input to lowercase to ignore uppercase/lowercase differences
    cleaned_input = user_input.lower().strip()

    # Rule-based response logic using if-elif-else
    if cleaned_input == "hello":
        return "Hi!"
    elif cleaned_input == "how are you":
        return "I'm fine, thanks!"
    elif cleaned_input == "what is your name":
        return "I am a simple chatbot."
    elif cleaned_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


# --- ADD THIS CODE AT THE BOTTOM TO RUN IT ---
print("Welcome to Basic Chatbot!")
while True:
    user_message = input("You: ")
    bot_message = get_bot_response(user_message)
    print(f"Bot: {bot_message}")
    
    if user_message.lower().strip() == "bye":
        break