from langgraph.prebuilt import create_react_agent
from typing import Literal
from langchain_tavily import TavilySearch
from langchain_openai import ChatOpenAI

tavily_tool = TavilySearch(max_results=5)
tavily_tool.invoke("What is JP Morgan's stock price?")['results']

from helper import agent_system_prompt

llm = ChatOpenAI(model="gpt-4o")

# Research agent and node
web_search_agent = create_react_agent(
    llm,
    tools=[tavily_tool],
    prompt=agent_system_prompt(f"""
        You are the Researcher. You can ONLY perform research 
        by using the provided search tool (tavily_tool). 
        When you have found the necessary information, end your output.  
        Do NOT attempt to take further actions.
    """),
)

agent_response = web_search_agent.invoke(
    {"messages":"what is jp morgan's current market cap?"})

agent_response['messages'][-1].content