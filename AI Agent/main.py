from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()
llm = ChatOpenAI()
response = llm.invoke("Explain AI agent in one line")
print(response.content)
