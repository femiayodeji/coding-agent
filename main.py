import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompt import system_prompt
from functions.call_function import available_functions, call_function

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
    
    config = types.GenerateContentConfig(
        system_instruction=system_prompt, 
        temperature=0,
        tools=[available_functions],
    )
    generate_content = client.models.generate_content(
        model=model, 
        contents=messages, 
        config=config
    )
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")     
        if generate_content.usage_metadata == None:
            raise RuntimeError("Usage metadata is None")
        print(f"Prompt tokens: {generate_content.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {generate_content.usage_metadata.candidates_token_count}")
    print(generate_content.text)

    if generate_content.function_calls:
        function_results = []
        for function_call in generate_content.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
            function_call_result = call_function(function_call, verbose=args.verbose)
            if function_call_result.parts[0].function_response == None:
                raise Exception("Function response is empty")
            if function_call_result.parts[0].function_response.response == None:
                raise Exception("Function response is empty")
            function_results.append(function_call_result.parts[0])
            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
            


if __name__ == "__main__":
    main()
