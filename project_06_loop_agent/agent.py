from google.adk.agents import Agent, LoopAgent


math_agent = Agent(
    name="MathQuestionAgent",
    model="gemini-2.5-flash",  # Or use LiteLLM: model=LiteLlm(model="openai/gpt-4o")
    description="An agent that asks math questions to the user.",
    instruction='Ask the user a math question.',
)

# Agent order is crucial: Critique first, then Refine/Exit
refinement_loop = LoopAgent(
    name="RefinementLoop",
    sub_agents=[math_agent],
    max_iterations=2 # Limit loops
)


root_agent = refinement_loop