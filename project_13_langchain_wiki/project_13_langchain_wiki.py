
import adk
from langchain.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

def run_wiki_bot():
    """Runs an agent that can answer questions using Wikipedia via LangChain."""
    try:
        # Create a LangChain tool for Wikipedia
        wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

        # Wrap the LangChain tool as an ADK tool
        wiki_tool = adk.LangChainTool(wikipedia)

        # Create an agent with the Wikipedia tool
        agent = adk.Agent(
            instructions="You are a helpful assistant that can answer questions using Wikipedia.",
            tools=[wiki_tool]
        )

        # Create a runner and start a chat session
        runner = adk.Runner()
        print("LangChain Wiki Bot is ready. Ask a question or type 'exit'.")

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
    run_wiki_bot()
