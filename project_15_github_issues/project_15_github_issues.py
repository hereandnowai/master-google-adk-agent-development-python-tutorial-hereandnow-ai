
import adk
import os

def run_github_issues_agent():
    """Runs an agent that can fetch open issues from a GitHub repository."""
    try:
        # Get the GitHub token from the environment variable
        github_token = os.environ.get("GITHUB_TOKEN")
        if not github_token:
            print("Error: GITHUB_TOKEN environment variable not set.")
            return

        # Create a GitHub toolset
        github_tools = adk.github.GitHub(token=github_token)

        # Create an agent with the GitHub toolset
        agent = adk.Agent(
            instructions="You are a helpful assistant that can list open issues in a GitHub repository.",
            tools=github_tools.get_tools()
        )

        # Create a runner and start a chat session
        runner = adk.Runner()
        print("GitHub Issues Agent is ready. Ask me to list open issues or type 'exit'.")

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
    run_github_issues_agent()
