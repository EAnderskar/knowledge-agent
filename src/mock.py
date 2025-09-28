from langchain_core.language_models import BaseChatModel
from langchain_core.outputs import ChatResult, ChatGeneration
from langchain_core.messages import AIMessage

class MockLLM(BaseChatModel):
    """A fake LLM that always returns a predictable response."""

    def _generate(self, messages, stop=None, run_manager=None, **kwargs):
        message = AIMessage(content="This is a reponse from a mock llm")
        generation = ChatGeneration(message=message)
        return ChatResult(generations=[generation])

    @property
    def _llm_type(self) -> str:
        return "mock-llm"

class MockWebSearch:
    """
    Mock Web Search MCP tool.
    """

    def __init__(self):
        pass

    def query(self, query_text: str):
        # In reality, here you would call Google Custom Search, SerpAPI, Bing, etc.
        # For now, we return a mock result
        return f"Mocked web search results for: {query_text}"
