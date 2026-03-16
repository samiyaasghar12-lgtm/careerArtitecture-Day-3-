# import
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_keys=os.getenv("GEMINI_API_KEYS")

genai.configure(api_key=api_keys)

# select modal
model=genai.GenerativeModel("gemini-2.5-flash-lite")

print("Chat started (Type 'exit' or 'bye' or 'quit')")
# apply while loop
while True:
    user_input=input("you!")
    if user_input in ['exit','bye','quit']:
        print("Goodbye! see you tomorrow!")
        break
    # user input passing
    response=model.generate_content(user_input)
    print("Agent:", response.text)