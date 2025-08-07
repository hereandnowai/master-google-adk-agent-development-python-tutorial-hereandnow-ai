import logging
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

logging.getLogger("LiteLLM").setLevel(logging.WARNING)
model = LiteLlm("ollama/llama3.1:8b")

hello_agent = Agent(
    name="GreetingAgent",
    model=model,
    description="A friendly assistant that greets the user.",
    instruction='First greet the user and then Answer user questions politely',
)

root_agent = hello_agent