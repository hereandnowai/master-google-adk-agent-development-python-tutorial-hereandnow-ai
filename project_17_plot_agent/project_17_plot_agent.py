
import adk
import matplotlib.pyplot as plt
import numpy as np

def plot_function(function_string: str, x_min: float, x_max: float) -> str:
    """Plots a mathematical function and saves it to a file."""
    try:
        x = np.linspace(x_min, x_max, 400)
        # A simple and unsafe way to evaluate the function string.
        # For a real application, use a safer parsing library.
        y = eval(function_string, {"x": x, "np": np})

        plt.figure()
        plt.plot(x, y)
        plt.title(f"Plot of {function_string}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.savefig("plot.png")

        return "The plot has been saved as plot.png"

    except Exception as e:
        return f"Error plotting function: {e}"

def run_plot_agent():
    """Runs an agent that can plot mathematical functions."""
    try:
        # Create a tool from the plot_function
        plot_tool = adk.FunctionTool(plot_function)

        # Create an agent with the plot tool
        agent = adk.Agent(
            instructions="You are a plotting assistant. Use the provided tool to plot functions.",
            tools=[plot_tool]
        )

        # Create a runner and start a chat session
        runner = adk.Runner()
        print("Plotting Agent is ready. Ask me to plot a function or type 'exit'.")

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
    run_plot_agent()
