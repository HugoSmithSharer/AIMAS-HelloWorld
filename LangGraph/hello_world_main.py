# Hello World agent for LangGraph using Azure OpenAI

import os
from dotenv import load_dotenv
load_dotenv("LangGraph/.env", override=True)
from langgraph.graph import StateGraph, END
from langchain.schema.messages import SystemMessage
from langchain_openai import AzureChatOpenAI

# Set up Azure OpenAI LLM using environment variables
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2023-05-15")  # Default version

llm = AzureChatOpenAI(
    openai_api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    deployment_name=AZURE_OPENAI_DEPLOYMENT,
    openai_api_version=AZURE_OPENAI_API_VERSION,
)

def product_manager_node(state):
    message = [
        SystemMessage(content="You are an experienced product manager with 8+ years of experience managing software products in high-growth startups. You excel at stakeholder collaboration, translating user needs into roadmap priorities, and balancing speed with quality. You believe in customer-centric product design and thrive in cross-functional environments. You will design and oversee product features, ensure user needs are met, and deliver a cohesive user experience that balances business viability and technical feasibility. Remember that you are a product manager and do not write code. You only decompose the feature as much as you can and pass to developers for implementation."),
        {"role": "user", "content": state["input"]}
    ]
    response = llm.invoke(message)
    state["tasks"] = response.content
    print("Response from product manager:", response.content)
    return state

def developer_node(state):
    message = [
        SystemMessage(content="You are a senior software engineer named DevX. You were trained on thousands of GitHub repositories and have years of experience shipping production-grade code. You work best with clear specs but can reverse-engineer unclear requests when needed. You value clean, maintainable code and always leave things better than you found them."),
        {"role": "user", "content": state["tasks"]}
    ]
    response = llm.invoke(message)
    print("Response from developer:", response.content)
    return state

graph = StateGraph(dict)
graph.add_node("product_manager", product_manager_node)
graph.add_node("developer", developer_node)
graph.add_edge("product_manager", "developer")
graph.add_edge("developer", END)
graph.set_entry_point("product_manager")

if __name__ == "__main__":
    compiled_graph = graph.compile()
    compiled_graph.invoke({"input": "I need your help to write a hello world with Python."})
