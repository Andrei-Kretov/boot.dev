import os, argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key=os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("api_key is not found")

CLIENT= genai.Client(api_key=api_key)
MODEL_ID = "gemini-2.5-flash"



def main():
    # Parse input
    parser= argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    #Send request to Gemini
    #Keeping track of conversation
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    response = CLIENT.models.generate_content(
        model = MODEL_ID, 
        contents = messages,
    )
    #Validate
    if response.usage_metadata == None:
        raise RuntimeError("Issue with API response")
    
    #Print
    if args.verbose:
        print(f"User prompt: {args.user_prompt}\nPrompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()
