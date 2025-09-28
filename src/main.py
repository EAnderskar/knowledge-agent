import os
from dotenv import load_dotenv

USE_MOCK = True

if USE_MOCK:
    from mock import MockLLM, MockWebSearch
    llm = MockLLM()
    web_search = MockWebSearch()
else:
    from langchain_openai import ChatOpenAI
    load_dotenv()
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

from graph import build_graph

graph = build_graph(llm, web_search)

result = graph.invoke({"input": "What is AI?"})
print(result)
