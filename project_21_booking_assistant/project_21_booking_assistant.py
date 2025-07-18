
import adk

# Dummy functions for booking
def book_flight(destination, dates): return f"Flight booked to {destination} for {dates}."
def book_hotel(destination, dates): return f"Hotel booked in {destination} for {dates}."
def book_car(destination, dates): return f"Car rented in {destination} for {dates}."

def run_booking_assistant():
    """Runs a multi-agent system for booking travel."""
    try:
        # Create tools for booking
        flight_tool = adk.FunctionTool(book_flight)
        hotel_tool = adk.FunctionTool(book_hotel)
        car_tool = adk.FunctionTool(book_car)

        # Create sub-agents for each booking task
        flight_agent = adk.Agent(instructions="Book a flight.", tools=[flight_tool])
        hotel_agent = adk.Agent(instructions="Book a hotel.", tools=[hotel_tool])
        car_agent = adk.Agent(instructions="Book a car.", tools=[car_tool])

        # Create a parallel workflow for booking
        booking_workflow = adk.Parallel([flight_agent, hotel_agent, car_agent])

        # Create a coordinator agent
        coordinator_agent = adk.Agent(
            instructions="You are a travel booking assistant. Use the provided agents to book a trip.",
            agents={"booking": booking_workflow}
        )

        # Create a runner and start a chat session
        runner = adk.Runner()
        print("Booking Assistant is ready. Ask me to book a trip or type 'exit'.")

        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break

            # Run the coordinator agent
            output = runner.run(coordinator_agent, user_input)
            print(f"Agent: {output}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_booking_assistant()
