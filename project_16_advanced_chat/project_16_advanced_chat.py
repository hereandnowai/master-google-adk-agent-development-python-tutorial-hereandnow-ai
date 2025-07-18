
import adk
import json

class LoggingCallback(adk.Callback):
    """A simple callback that logs the agent's actions."""
    def on_agent_step(self, step, **kwargs):
        print(f"Agent Step: {step}")

class FileSessionService(adk.SessionService):
    """A session service that stores conversation history in a file."""
    def __init__(self, file_path="session.json"):
        self.file_path = file_path

    def load(self, session_id):
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save(self, session_id, history):
        with open(self.file_path, "w") as f:
            json.dump(history, f)

def run_advanced_chat():
    """Runs a chatbot with logging and file-based memory."""
    try:
        # Create an agent
        agent = adk.Agent(
            instructions="You are a friendly assistant."
        )

        # Create a runner with the logging callback and file session service
        runner = adk.Runner(
            callbacks=[LoggingCallback()],
            session_service=FileSessionService()
        )

        print("Advanced Chatbot is ready. Talk to it or type 'exit'.")

        # Start a chat session
        with runner.chat() as session:
            while True:
                user_input = input("You: ")
                if user_input.lower() == "exit":
                    print("Exiting...")
                    break

                # Run the agent with the user's input
                output = session.run(agent, user_input)
                print(f"Agent: {output}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_advanced_chat()
