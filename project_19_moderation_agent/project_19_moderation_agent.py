
import adk

BANNED_WORDS = ["bad", "word"]

def check_for_banned_words(text: str) -> bool:
    """Checks if the text contains any banned words."""
    return any(word in text.lower() for word in BANNED_WORDS)

def run_moderation_agent():
    """Runs a content moderation agent."""
    try:
        # Create a normal agent
        normal_agent = adk.Agent(
            instructions="You are a friendly assistant."
        )

        # Create a moderation agent
        moderation_agent = adk.Agent(
            instructions="Warn the user that their message is inappropriate."
        )

        # Create a router that decides which agent to use
        def router(user_input):
            if check_for_banned_words(user_input):
                return moderation_agent
            else:
                return normal_agent

        # Create a runner and start a chat session
        runner = adk.Runner()
        print("Moderation Agent is ready. Say something or type 'exit'.")

        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break

            # Route the input to the appropriate agent
            agent_to_use = router(user_input)
            output = runner.run(agent_to_use, user_input)
            print(f"Agent: {output}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_moderation_agent()
