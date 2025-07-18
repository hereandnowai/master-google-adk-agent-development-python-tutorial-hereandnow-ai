
import adk

def run_parallel_agents():
    """Demonstrates running two agents in parallel."""
    try:
        # Define the weather agent
        weather_agent = adk.Agent(
            instructions="Get the weather for a given city.",
            tools=[adk.google_search]
        )

        # Define the news agent
        news_agent = adk.Agent(
            instructions="Get the latest news on a given topic.",
            tools=[adk.google_search]
        )

        # Create a parallel workflow
        workflow = adk.Parallel(
            [weather_agent, news_agent]
        )

        # Create a runner and start a chat session
        runner = adk.Runner()
        print("Parallel Agent is ready. Enter a city and a news topic or type 'exit'.")

        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break

            # Run the workflow with the user's input
            output = runner.run(workflow, user_input)
            print(f"Agent: {output}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_parallel_agents()
