
import adk
import time

class TimingCallback(adk.Callback):
    """A callback that times the execution of each agent step."""
    def __init__(self):
        self.start_time = None

    def on_agent_step(self, step, **kwargs):
        if self.start_time:
            end_time = time.time()
            print(f"Step finished in {end_time - self.start_time:.2f} seconds.")
        self.start_time = time.time()

def run_performance_tuning():
    """Demonstrates how to profile and tune an agent's performance."""
    try:
        # Create an agent
        agent = adk.Agent(
            instructions="You are a helpful assistant."
        )

        # Create a runner with the timing callback
        runner = adk.Runner(callbacks=[TimingCallback()])

        # Run the agent with some input
        runner.run(agent, "Hello")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_performance_tuning()
