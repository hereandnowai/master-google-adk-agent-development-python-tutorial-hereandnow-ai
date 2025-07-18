
import adk
import threading

def run_scalable_network():
    """Simulates a scalable agent network."""
    try:
        # Create a simple agent
        agent = adk.Agent(
            instructions="You are a helpful assistant."
        )

        # Define a function to run an agent instance
        def run_agent_instance(instance_id, user_input):
            runner = adk.Runner()
            output = runner.run(agent, user_input)
            print(f"Instance {instance_id}: {output}")

        # Simulate multiple user requests
        user_requests = ["Hello", "How are you?", "What is your name?"]

        # Create and start a thread for each user request
        threads = []
        for i, request in enumerate(user_requests):
            thread = threading.Thread(target=run_agent_instance, args=(i, request))
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_scalable_network()
