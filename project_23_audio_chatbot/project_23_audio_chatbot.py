
import adk
import time

def run_audio_chatbot():
    """Simulates a real-time audio chatbot."""
    try:
        # Create an agent
        agent = adk.Agent(
            instructions="You are a voice assistant. You can perform actions like setting a timer."
        )

        # Create a runner
        runner = adk.Runner()
        print("Audio Chatbot is ready. Speak your commands (type them) or type 'exit'.")

        # Simulate a streaming audio session
        with runner.stream() as stream:
            while True:
                user_input = input("You: ")
                if user_input.lower() == "exit":
                    print("Exiting...")
                    break

                # Send the user's input to the stream
                stream.send(agent, user_input)

                # Process the stream
                for output in stream:
                    print(f"Agent: {output}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_audio_chatbot()
