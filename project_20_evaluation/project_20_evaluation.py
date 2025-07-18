
import adk

def run_evaluation_pipeline():
    """Runs an evaluation pipeline for a simple Q&A agent."""
    try:
        # Create a simple Q&A agent
        agent = adk.Agent(
            instructions="You are a question-answering assistant."
        )

        # Define a dataset of questions and expected answers
        dataset = [
            {
                "input": "What is the capital of France?",
                "expected_output": "Paris"
            },
            {
                "input": "What is 2 + 2?",
                "expected_output": "4"
            }
        ]

        # Create an evaluator
        evaluator = adk.Evaluator()

        # Run the evaluation
        results = evaluator.run(agent, dataset)

        # Print the evaluation results
        print("Evaluation Results:")
        for result in results:
            print(f"Input: {result.input}")
            print(f"Output: {result.output}")
            print(f"Expected Output: {result.expected_output}")
            print(f"Correct: {result.is_correct()}")
            print("---")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_evaluation_pipeline()
