from google.adk.agents import Agent
from google.adk.tools import google_search

search_agent = Agent(
    name="SearchAgent",
    model="gemini-2.5-flash",  # Or use LiteLLM: model=LiteLlm(model="openai/gpt-4o")
    description="A friendly assistant that greets the user.",  # Optional description
    instruction='You are a helpful assistant. Answer user questions using Google Search when needed.',
    tools=[google_search]
)

root_agent = search_agent
