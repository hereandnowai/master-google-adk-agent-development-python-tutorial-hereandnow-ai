
import adk

def run_sequential_workflow():
    """Demonstrates a sequential workflow with two tasks."""
    try:
        # Define the first task: searching for a topic
        search_task = adk.Agent(
            instructions="Search for the given topic and return the results.",
            tools=[adk.google_search]
        )

        # Define the second task: summarizing the search results
        summarize_task = adk.Agent(
            instructions="Summarize the input text."
        )

        # Create a sequential workflow
        workflow = adk.Sequential(
            [search_task, summarize_task]
        )

        # Create a runner and start a chat session
        runner = adk.Runner()
        print("Sequential Workflow Agent is ready. Enter a topic to research or type 'exit'.")

        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break

            # Run the workflow with the user's input
            output = runner.run(workflow, user_input)
            print(f"Agent: {output}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_sequential_workflow()
