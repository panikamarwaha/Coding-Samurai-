import openai

openai.api_key = "your_api_key_here"
messages = []

# System prompt to initiate the conversation
system_msg = "What type of chatbot would you like to create?"
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")

while True:
    # User input
    user_input = input("User: ")

    # Check for exit condition
    if user_input.lower() == "quit()":
        break

    # Append user message to the conversation
    messages.append({"role": "user", "content": user_input})

    # Assistant's response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    reply = response["choices"][0]["message"]["content"]

    # Append assistant's reply to the conversation
    messages.append({"role": "assistant", "content": reply})

    # Print the assistant's response
    print("Bot:", reply)
