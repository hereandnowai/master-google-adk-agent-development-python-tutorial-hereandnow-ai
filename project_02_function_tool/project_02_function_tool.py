import adk

def convert_units(quantity: float, from_unit: str, to_unit: str) -> str:
    """Converts a quantity from one unit to another.

    Args:
        quantity: The numerical value to convert.
        from_unit: The starting unit (e.g., "km").
        to_unit: The target unit (e.g., "miles").

    Returns:
        A string describing the result of the conversion.
    """
    try:
        # Conversion factors
        factors = {
            "km": {"miles": 0.621371},
            "miles": {"km": 1.60934},
        }

        # Perform the conversion
        factor = factors[from_unit][to_unit]
        result = quantity * factor
        return f"{quantity} {from_unit} is equal to {result:.4f} {to_unit}."

    except KeyError:
        return f"Conversion from {from_unit} to {to_unit} is not supported."
    except Exception as e:
        return f"An error occurred during conversion: {e}"

def run_conversion_agent():
    """Runs an agent that uses the unit conversion tool."""
    try:
        # Create a tool from the Python function
        conversion_tool = adk.FunctionTool(convert_units)

        # Create an agent with the conversion tool
        agent = adk.Agent(
            instructions="You are a helpful assistant that converts units.",
            tools=[conversion_tool]
        )

        # Create a runner and start a chat session
        runner = adk.Runner()
        print("Unit Conversion Agent is ready. Type your conversion query or 'exit'.")

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
    run_conversion_agent()