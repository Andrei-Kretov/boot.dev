import os
from dotenv import load_dotenv
from google import genai


load_dotenv()
try :
    api_key=os.environ.get("GEMINI_API_KEY")
except KeyError:
    raise RuntimeError("api_key is not found")

CLIENT= genai.Client(api_key=api_key)
MODEL_ID = "gemini-2.5-flash"
PROMT = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."



def main():
    response = CLIENT.models.generate_content(
        model = MODEL_ID,
        contents = PROMT,
    )
    print(response.text)


if __name__ == "__main__":
    main()
