
import adk

def run_search_agent():
    """Runs an agent that can use the built-in Google Search tool."""
    try:
        # Create an agent and add the google_search tool
        agent = adk.Agent(
            instructions="You are a helpful assistant that can search the web.",
            tools=[adk.google_search]
        )

        # Create a runner and start a chat session
        runner = adk.Runner()
        print("Search Agent is ready. Ask a question or type 'exit'.")

        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break

            # Run the agent with the user's input
            output = runner.run(agent, user_input)
            print(f"Agent: {output}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_search_agent()
