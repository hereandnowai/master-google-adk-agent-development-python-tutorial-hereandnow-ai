from google.adk.agents import Agent

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

tool_agent = Agent(
    name="ToolAgent",
    model="gemini-2.5-flash",  # Or use LiteLLM: model=LiteLlm(model="openai/gpt-4o")
    description="Tool to convert_units .",  # Optional description
    instruction='You are a helpful assistant that converts units. always use the tool convert_units',
    tools=[convert_units]
)
root_agent = tool_agent