import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# Store conversation history
conversation_history = []

# Define chatbot instructions
SYSTEM_PROMPT = """
You are an intelligent AI chatbot.
Answer user questions clearly and accurately.
Maintain conversational context.
Provide meaningful and relevant responses.
Use simple language whenever possible.
"""

# Function to generate response
def generate_response(user_input):

    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    response = client.responses.create(
        model="gpt-5",
        instructions=SYSTEM_PROMPT,
        input=conversation_history
    )

    bot_reply = response.output_text

    conversation_history.append({
        "role": "assistant",
        "content": bot_reply
    })

    return bot_reply


# Main chatbot function
def chatbot():

    print("=" * 50)
    print("       INTELLIGENT AI CHATBOT")
    print("=" * 50)

    print("Bot: Hello! Welcome to the AI chatbot.")
    print("Bot: Ask me anything.")
    print("Bot: Type 'exit' to end the conversation.\n")

    while True:

        user_input = input("You: ").strip()

        # Check for empty input
        if not user_input:
            print("Bot: Please enter a valid message.\n")
            continue

        # Exit condition
        if user_input.lower() == "exit":
            print("\nBot: Thank you for chatting. Goodbye!")
            break

        try:

            # Generate AI response
            bot_reply = generate_response(user_input)

            # Display response
            print("\nBot:", bot_reply)
            print()

        except Exception as e:

            print("\nBot: An error occurred.")
            print("Error:", e)
            print()


# Execute chatbot
if __name__ == "__main__":
    chatbot()