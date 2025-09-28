from typing import TypedDict
from langgraph.graph import StateGraph

# Definiera state schema
class AgentState(TypedDict):
    input: str
    llm_output: str
    web_result: str
    plot_path: str

def build_graph(llm, web_search):
    workflow = StateGraph(AgentState)

    # --- Nod 1: LLM ---
    def ask_llm(state: AgentState):
        user_input = state.get("input", "")
        response = llm.invoke(user_input)
        return {"llm_output": response.content}
    
    # --- Nod 2: WebSearch ---
    def web_search_node(state:AgentState):
        query = state.get("input", "")
        print(query)
        result = web_search.query(query)
        print(result)
        return {"web_result": result}

    # --- Nod 3: Plot (mock) ---
    def create_plot(state: AgentState):
        return {"plot_path": "plots/mock_plot.png"}

    workflow.add_node("llm", ask_llm)
    workflow.add_node("web_search", web_search_node)
    workflow.add_node("plot", create_plot)

    workflow.set_entry_point("llm")
    workflow.add_edge("llm", "web_search")
    workflow.add_edge("web_search", "plot")
    workflow.set_finish_point("plot")

    return workflow.compile()
