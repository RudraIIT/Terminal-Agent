import os
import signal
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

def signal_handler(sig, frame):
    print("\n Agent Stopped")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def main():
    print("Shell Assistant Agent Started. Type 'exit' to stop.")

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    while True:
        user_input = input("Ask: ")
        if user_input.strip().lower() in ['exit', 'quit']:
            print("Exiting...")
            break

        
        prompt = f"You are a Linux shell expert. Convert the following request into the appropriate Ubuntu shell command only, no explanation:\n\n\"{user_input}\""

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config=types.GenerateContentConfig(
                    thinking_config=types.ThinkingConfig(thinking_budget=0)
                )
            )
            command = response.text.strip().strip("`")
            confirm = input(f"Do you want to execute this {command} command? (y/n): ")
            if confirm.lower() == 'y':
                os.system(command)
            else:
                print("Command execution cancelled.")
        except:
            print("Error: Unable to process the request.")
    
if __name__ == "__main__":
    main()
