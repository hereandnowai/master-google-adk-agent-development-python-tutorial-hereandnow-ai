from google.adk.agents import Agent

hello_agent = Agent(
    name="GreetingAgent",
    model="gemini-2.5-flash",  # Or use LiteLLM: model=LiteLlm(model="openai/gpt-4o")
    description="A friendly assistant that greets the user.",  # Optional description
    instruction='First greet the user and then Answer user questions politely',
)

root_agent = hello_agent
