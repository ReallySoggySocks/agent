import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.config import *

messages = [
    types.Content(role="user", parts=[types.Part(text=sys.argv[1])])
]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    if len(sys.argv) < 2:
        print("No prompt was given")
        sys.exit(1)
    else:
        response = client.models.generate_content(model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=SYSTEM_PROMPT)
        )

        if response.function_calls != None:
            for function in response.function_calls:
                print(f"Calling Function: {function.name}({function.args})")

        elif "--verbose" in sys.argv:
            print(
f"""
User prompt: {sys.argv[1]}

Response: {response.text}

Prompt tokens: {response.usage_metadata.prompt_token_count}
Response tokens: {response.usage_metadata.candidates_token_count}
"""
                  )
        else:
            print(response.text)


if __name__ == "__main__":
    main()
