import adk

def run_hello_agent():
    """
    Initializes and runs a simple ADK agent that prints a greeting.
    """
    try:
        # Define the instruction for the agent.
        # This is a simple prompt that tells the agent what to do.
        agent = adk.Agent(instructions="You are a friendly assistant that greets the user.")

        # Use the Runner to execute the agent's task.
        # The Runner manages the lifecycle of the agent.
        runner = adk.Runner()
        print("Running Hello Agent...")
        output = runner.run(agent, "Hello!")

        # Print the output from the agent.
        print(f"Agent Response: {output}")

    except Exception as e:
        # Handle any exceptions that may occur during the process.
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Entry point of the script.
    run_hello_agent()