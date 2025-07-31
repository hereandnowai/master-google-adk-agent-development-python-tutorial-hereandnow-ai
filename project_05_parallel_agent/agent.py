from google.adk.agents import Agent, ParallelAgent
from google.adk.tools import google_search


 # Define the first task: searching for a topic
search_agent1 = Agent(
    name="SearchAgent",
    model="gemini-2.5-flash",  # Or use LiteLLM: model=LiteLlm(model="openai/gpt-4o")
    description="Gets the latest news on a given topic.",  # Optional description
    instruction='Get the latest news on a given topic.',
    tools=[google_search]
)

 # Define the first task: searching for a topic
search_agent2 = Agent(
    name="SearchAgent",
    model="gemini-2.5-flash",  # Or use LiteLLM: model=LiteLlm(model="openai/gpt-4o")
    description="Gets the weather for a given city.",  # Optional description
    instruction='Get the weather for a given city.',
    tools=[google_search]
)

# Create a parallel workflow
parallel_agent = ParallelAgent(
    name="ParallelAgent",
    sub_agents=[search_agent1, search_agent2],
    description="A parallel agent that retrieves weather and news information.",
)

root_agent = parallel_agent