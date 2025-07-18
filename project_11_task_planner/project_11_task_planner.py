
import adk

def run_task_planner():
    """Demonstrates a multi-step task planning agent."""
    try:
        # Define the agent that breaks down a goal into tasks
        planner_agent = adk.Agent(
            instructions="You are a project planner. Break down the given goal into a list of tasks."
        )

        # Create a runner and start a chat session
        runner = adk.Runner()
        print("Task Planner is ready. Enter a goal to plan or type 'exit'.")

        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break

            # Run the agent with the user's input
            output = runner.run(planner_agent, user_input)
            print(f"Agent: {output}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_task_planner()
