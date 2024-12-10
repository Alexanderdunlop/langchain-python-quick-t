import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    HumanMessagePromptTemplate,
    ChatPromptTemplate
)
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser

class ProjectIdea(BaseModel):
    title: str = Field(description="Title of the project")
    description: str = Field(description="Description of the project")
    packages: str = Field(description="Packages required for the project")

load_dotenv()

OPENAI_MODEL = "gpt-4"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

PROMPT_CODING_PROJECT_INFO = """
    Provide me with project ideas using {language}.
    {format_instructions}
    """

def main():
    llm = ChatOpenAI(api_key=OPENAI_API_KEY, model=OPENAI_MODEL)
    parser = PydanticOutputParser(pydantic_object=ProjectIdea)

    language = input("Enter the programming language: ")

    message = HumanMessagePromptTemplate.from_template(template=PROMPT_CODING_PROJECT_INFO)
    chat_prompt = ChatPromptTemplate.from_messages(messages=[message])
    chat_prompt_with_values = chat_prompt.format_prompt(
        language=language,
        format_instructions=parser.get_format_instructions()
    )

    response = llm(messages=chat_prompt_with_values.to_messages())
    data = parser.invoke(response.content)
    print(data)

if __name__ == "__main__":
    main()