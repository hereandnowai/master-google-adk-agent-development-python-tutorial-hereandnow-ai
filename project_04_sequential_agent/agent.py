from google.adk.agents import Agent, SequentialAgent
from google.adk.tools import google_search

 # Define the first task: searching for a topic
search_agent = Agent(
    name="SearchAgent",
    model="gemini-2.5-flash",  # Or use LiteLLM: model=LiteLlm(model="openai/gpt-4o")
    description="A friendly assistant that greets the user.",  # Optional description
    instruction='You are a helpful assistant. Answer user questions using Google Search when needed.',
    tools=[google_search]
)

# Define the second task: summarizing the search results
summerizing_agent = Agent(
    name="SummerizingAgent",
    model="gemini-2.5-flash",  # Or use LiteLLM: model=LiteLlm(model="openai/gpt-4o")
    description="Summerizing Agent",  # Optional description
    instruction='Summarize the input text.',
    tools=[google_search]
)

search_pipeline_agent = SequentialAgent(
    name="search_pipeline_agent",
    sub_agents=[search_agent, summerizing_agent],
    description="A pipeline agent that searches for a topic and summarizes the results.",
)

root_agent = search_pipeline_agent
