import os

from dotenv import load_dotenv

from langchain_openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def main():
    llm = OpenAI(api_key=OPENAI_API_KEY)
    result = llm.predict("translate English to French: Hello, how are you?")
    print(result)

if __name__ == "__main__":
    main()