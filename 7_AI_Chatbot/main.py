# api limit exhausted


from google import genai
from google.api_core import exceptions
import time

# 1. Setup the client
client = genai.Client(api_key="put_your_api_key_here")

# 2. Start a chat session 
# Note: Using 'gemini-1.5-flash' is usually the most stable for free tier
try:
    chat = client.chats.create(model="gemini-1.5-flash")
except Exception as e:
    # If gemini-1.5-flash fails, try the full path
    chat = client.chats.create(model="models/gemini-1.5-flash")

print("--- AI Chatbot (Type 'exit' to stop) ---")

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye!")
        break

    try:
        response = chat.send_message(user_input)
        print(f"Bot: {response.text}")
        
    except exceptions.ResourceExhausted:
        print("Bot: System is busy (Quota hit). Please wait 60 seconds...")
        time.sleep(60)
    except Exception as e:
        print(f"Error: {e}")