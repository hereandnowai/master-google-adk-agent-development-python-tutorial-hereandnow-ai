
import adk
import os

def run_code_reviewer():
    """Runs a code review assistant."""
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
            instructions="You are a code review assistant. Use the provided tools to review code.",
            tools=github_tools.get_tools()
        )

        # Create a runner and start a chat session
        runner = adk.Runner()
        print("Code Review Assistant is ready. Ask me to review a repository or type 'exit'.")

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
    run_code_reviewer()
