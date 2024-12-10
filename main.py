import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    HumanMessagePromptTemplate,
    ChatPromptTemplate
)

load_dotenv()

OPENAI_MODEL = "gpt-4"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

PROMPT_CODING_PROJECT_INFO = """
    Provide me with project ideas using {language}.
    """

def main():
    llm = ChatOpenAI(api_key=OPENAI_API_KEY, model=OPENAI_MODEL)

    language = input("Enter the programming language: ")

    message = HumanMessagePromptTemplate.from_template(template=PROMPT_CODING_PROJECT_INFO)
    chat_prompt = ChatPromptTemplate.from_messages(messages=[message])
    chat_prompt_with_values = chat_prompt.format_prompt(language=language)

    response = llm(messages=chat_prompt_with_values.to_messages())
    print(response)

if __name__ == "__main__":
    main()