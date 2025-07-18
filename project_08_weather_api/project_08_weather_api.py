
import adk
import requests

# Replace "YOUR_API_KEY" with your actual OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"

def get_weather(city: str) -> str:
    """Fetches the current weather for a given city using the OpenWeatherMap API."""
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        data = response.json()
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]

        return f"The weather in {city} is currently {weather_description} with a temperature of {temperature}°C."

    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"
    except KeyError:
        return f"Could not find weather data for {city}."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def run_weather_agent():
    """Runs an agent that can fetch weather information."""
    try:
        # Create a tool from the get_weather function
        weather_tool = adk.FunctionTool(get_weather)

        # Create an agent with the weather tool
        agent = adk.Agent(
            instructions="You are a weather assistant. Use the provided tool to get the weather.",
            tools=[weather_tool]
        )

        # Create a runner and start a chat session
        runner = adk.Runner()
        print("Weather Agent is ready. Ask for the weather or type 'exit'.")

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
    run_weather_agent()
