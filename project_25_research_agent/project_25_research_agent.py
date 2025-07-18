
import adk

def run_research_agent():
    """Runs an autonomous research agent."""
    try:
        # Define the sub-agents for the research tasks
        search_agent = adk.Agent(
            instructions="Search for information on the given topic.",
            tools=[adk.google_search]
        )
        summarize_agent = adk.Agent(
            instructions="Summarize the given text."
        )

        # Define the research workflow
        research_workflow = adk.Sequential([search_agent, summarize_agent])

        # Define the planner agent
        planner_agent = adk.Agent(
            instructions="You are a research assistant. Create a plan to research the given topic.",
            agents={"research": research_workflow}
        )

        # Create a runner and start a chat session
        runner = adk.Runner()
        print("Research Agent is ready. Enter a research query or type 'exit'.")

        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break

            # Run the planner agent
            output = runner.run(planner_agent, user_input)
            print(f"Agent: {output}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_research_agent()
