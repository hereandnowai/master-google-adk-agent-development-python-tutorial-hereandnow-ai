
import adk

def search_flights(destination: str, dates: str) -> str:
    """Searches for flights to a destination on given dates (dummy data)."""
    return f"Found a flight to {destination} on {dates} for $500."

def search_hotels(destination: str, dates: str) -> str:
    """Searches for hotels in a destination for given dates (dummy data)."""
    return f"Found a hotel in {destination} for {dates} for $100 per night."

def run_travel_planner():
    """Runs a travel itinerary planning agent."""
    try:
        # Create tools from the search functions
        flight_tool = adk.FunctionTool(search_flights)
        hotel_tool = adk.FunctionTool(search_hotels)

        # Create agents for flights and hotels
        flight_agent = adk.Agent(
            instructions="Search for flights.",
            tools=[flight_tool]
        )
        hotel_agent = adk.Agent(
            instructions="Search for hotels.",
            tools=[hotel_tool]
        )

        # Create a parallel workflow to search for flights and hotels simultaneously
        search_workflow = adk.Parallel([flight_agent, hotel_agent])

        # Create a master agent to generate the itinerary
        itinerary_agent = adk.Agent(
            instructions="Create a travel itinerary from the flight and hotel information.",
            agents={"search": search_workflow}
        )

        # Create a runner and start a chat session
        runner = adk.Runner()
        print("Travel Planner is ready. Enter your destination and dates or type 'exit'.")

        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break

            # Run the itinerary agent with the user's input
            output = runner.run(itinerary_agent, user_input)
            print(f"Agent: {output}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_travel_planner()
