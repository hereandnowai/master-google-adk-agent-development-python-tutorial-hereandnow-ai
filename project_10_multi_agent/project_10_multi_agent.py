
import adk

def run_multi_agent_pipeline():
    """Demonstrates a master agent that delegates tasks to sub-agents."""
    try:
        # Define the sub-agent for finding activities
        activities_agent = adk.Agent(
            instructions="Find fun activities in the given city.",
            tools=[adk.google_search]
        )

        # Define the sub-agent for finding restaurants
        restaurants_agent = adk.Agent(
            instructions="Find good restaurants in the given city.",
            tools=[adk.google_search]
        )

        # Define the master agent that delegates to the sub-agents
        master_agent = adk.Agent(
            instructions="You are a weekend planner. Use the activities and restaurants agents to create a plan.",
            agents={
                "activities": activities_agent,
                "restaurants": restaurants_agent
            }
        )

        # Create a runner and start a chat session
        runner = adk.Runner()
        print("Multi-Agent Planner is ready. Ask me to plan a weekend or type 'exit'.")

        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break

            # Run the master agent with the user's input
            output = runner.run(master_agent, user_input)
            print(f"Agent: {output}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_multi_agent_pipeline()
