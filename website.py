import openai
import gradio

openai.api_key = "your_api_key_here"

# Initial system message
system_msg = "You are a real estate investment expert. Provide information and insights on real estate investment and negotiation."

messages = [{"role": "system", "content": system_msg}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})

    try:
        # Request completion from OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Extract assistant's reply
        ChatGPT_reply = response["choices"][0]["message"]["content"]

        # Append assistant's reply to the conversation
        messages.append({"role": "assistant", "content": ChatGPT_reply})

        return ChatGPT_reply

    except Exception as e:
        # Handle API request errors gracefully
        return f"An error occurred: {str(e)}"

# Gradio interface setup
demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Real Estate Pro")

# Launch the Gradio interface
demo.launch(share=True)
