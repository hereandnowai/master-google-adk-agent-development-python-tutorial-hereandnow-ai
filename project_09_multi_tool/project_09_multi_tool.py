
import adk

def calculate(expression: str) -> str:
    """Calculates the result of a mathematical expression."""
    try:
        # A simple and unsafe way to evaluate math expressions.
        # For a real application, use a safer parsing library.
        result = eval(expression)
        return f"The result of the calculation is: {result}"
    except Exception as e:
        return f"Error performing calculation: {e}"

def run_multi_tool_agent():
    """Runs an agent that can use both search and a custom math tool."""
    try:
        # Create a tool from the calculate function
        math_tool = adk.FunctionTool(calculate)

        # Create an agent with multiple tools
        agent = adk.Agent(
            instructions="You are a helpful assistant. Use the search tool for questions and the math tool for calculations.",
            tools=[adk.google_search, math_tool]
        )

        # Create a runner and start a chat session
        runner = adk.Runner()
        print("Multi-Tool Agent is ready. Ask a question or a calculation, or type 'exit'.")

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
    run_multi_tool_agent()
