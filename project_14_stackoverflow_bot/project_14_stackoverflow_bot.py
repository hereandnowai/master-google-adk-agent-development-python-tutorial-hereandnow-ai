
import adk
from langchain.tools import StackExchangeTool

def run_stackoverflow_bot():
    """Runs an agent that can answer programming questions using the StackExchange API."""
    try:
        # Create a LangChain tool for StackExchange
        stack_exchange_tool = StackExchangeTool()

        # Wrap the LangChain tool as an ADK tool
        adk_tool = adk.LangChainTool(stack_exchange_tool)

        # Create an agent with the StackExchange tool
        agent = adk.Agent(
            instructions="You are a helpful assistant that answers programming questions using StackOverflow.",
            tools=[adk_tool]
        )

        # Create a runner and start a chat session
        runner = adk.Runner()
        print("StackOverflow Bot is ready. Ask a programming question or type 'exit'.")

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
    run_stackoverflow_bot()
