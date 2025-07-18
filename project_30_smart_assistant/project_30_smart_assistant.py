
import adk
import os

# Dummy function for scheduling
def schedule_meeting(attendees, time, topic): return f"Meeting scheduled with {attendees} at {time} to discuss {topic}."

def run_smart_assistant():
    """Runs a capstone smart assistant."""
    try:
        # Create a document store for RAG
        document_store = adk.VectorStore(
            adk.loaders.DirectoryLoader("documents"),
            adk.embeddings.GoogleGenerativeAIEmbeddings(),
            adk.vector_stores.Faiss()
        )

        # Create a RAG agent
        rag_agent = adk.RAG(
            document_store=document_store,
            instructions="Answer questions about the provided documents."
        )

        # Create a scheduling tool
        schedule_tool = adk.FunctionTool(schedule_meeting)

        # Create a scheduling agent
        schedule_agent = adk.Agent(
            instructions="Schedule meetings.",
            tools=[schedule_tool]
        )

        # Create a master agent
        master_agent = adk.Agent(
            instructions="You are a smart assistant. You can answer questions about documents and schedule meetings.",
            agents={
                "rag": rag_agent,
                "schedule": schedule_agent
            }
        )

        # Create a runner with memory
        runner = adk.Runner(session_service=adk.InMemorySessionService())

        print("Smart Assistant is ready. Ask me anything or type 'exit'.")

        # Start a chat session
        with runner.chat() as session:
            while True:
                user_input = input("You: ")
                if user_input.lower() == "exit":
                    print("Exiting...")
                    break

                # Run the master agent
                output = session.run(master_agent, user_input)
                print(f"Agent: {output}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Create a dummy documents directory for the example
    if not os.path.exists("documents"):
        os.makedirs("documents")
        with open("documents/travel_guide.txt", "w") as f:
            f.write("Paris is the capital of France.")

    run_smart_assistant()
