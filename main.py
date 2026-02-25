import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main():

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    client = genai.Client(api_key=api_key)

    model = "gemini-2.5-flash"
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    generate_content = client.models.generate_content(model=model, contents=messages)
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")     
        if generate_content.usage_metadata == None:
            raise RuntimeError("Usage metadata is None")
        print(f"Prompt tokens: {generate_content.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {generate_content.usage_metadata.candidates_token_count}")
    print(generate_content.text)


if __name__ == "__main__":
    main()
