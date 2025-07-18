
import adk

def run_chat_agent_with_memory():
    """Demonstrates a chat agent that remembers conversation history."""
    try:
        # Create an agent
        agent = adk.Agent(
            instructions="You are a friendly assistant that remembers the user's name."
        )

        # Create a runner and a session service for memory
        runner = adk.Runner(session_service=adk.InMemorySessionService())
        print("Chat Agent with Memory is ready. Talk to it or type 'exit'.")

        # Start a chat session
        with runner.chat() as session:
            while True:
                user_input = input("You: ")
                if user_input.lower() == "exit":
                    print("Exiting...")
                    break

                # Run the agent with the user's input
                output = session.run(agent, user_input)
                print(f"Agent: {output}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_chat_agent_with_memory()
