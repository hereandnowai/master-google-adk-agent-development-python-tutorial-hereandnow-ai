
import adk

def run_a2a_collaboration():
    """Demonstrates Agent-to-Agent (A2A) collaboration."""
    try:
        # Define the data provider agent
        data_agent = adk.Agent(
            instructions="You are a data provider. You provide data to other agents."
        )

        # Define the data analysis agent
        analysis_agent = adk.Agent(
            instructions="You are a data analyst. You analyze data provided by other agents."
        )

        # Define the master agent that facilitates the collaboration
        master_agent = adk.Agent(
            instructions="You are a master agent. Use the data and analysis agents to solve problems.",
            agents={
                "data": data_agent,
                "analysis": analysis_agent
            }
        )

        # Create a runner and start a chat session
        runner = adk.Runner()
        print("A2A Collaboration is ready. Enter a problem or type 'exit'.")

        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break

            # Run the master agent
            output = runner.run(master_agent, user_input)
            print(f"Agent: {output}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_a2a_collaboration()
