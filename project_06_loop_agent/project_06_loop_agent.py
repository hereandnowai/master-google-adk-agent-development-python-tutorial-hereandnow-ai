
import adk

def run_loop_agent():
    """Demonstrates a loop agent that continues until a condition is met."""
    try:
        # Define the agent that asks math questions
        math_agent = adk.Agent(
            instructions="Ask the user a math question."
        )

        # Create a loop that continues until the user says "exit"
        workflow = adk.Loop(
            math_agent,
            until="[user_input] == 'exit'"
        )

        # Create a runner and start the loop
        runner = adk.Runner()
        print("Loop Agent is ready. Answer the math questions or type 'exit' to stop.")

        # Run the workflow
        runner.run(workflow)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_loop_agent()
