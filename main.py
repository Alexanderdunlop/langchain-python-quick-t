import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

load_dotenv()

OPENAI_MODEL = "gpt-4"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def main():
    llm = ChatOpenAI(api_key=OPENAI_API_KEY, model=OPENAI_MODEL)
    result = llm.predict("Give me 5 project ideas for Python.")
    print(result)

if __name__ == "__main__":
    main()