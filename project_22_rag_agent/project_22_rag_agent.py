
import adk
import os

def run_rag_agent():
    """Runs a Retrieval-Augmented Generation (RAG) agent."""
    try:
        # Create a document store
        document_store = adk.VectorStore(
            adk.loaders.DirectoryLoader("documents"),
            adk.embeddings.GoogleGenerativeAIEmbeddings(),
            adk.vector_stores.Faiss()
        )

        # Create a RAG agent
        agent = adk.RAG(
            document_store=document_store,
            instructions="You are a helpful assistant that answers questions about the provided documents."
        )

        # Create a runner and start a chat session
        runner = adk.Runner()
        print("RAG Agent is ready. Ask a question about the documents or type 'exit'.")

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
    # Create a dummy documents directory for the example
    if not os.path.exists("documents"):
        os.makedirs("documents")
        with open("documents/doc1.txt", "w") as f:
            f.write("The sky is blue.")
        with open("documents/doc2.txt", "w") as f:
            f.write("The grass is green.")

    run_rag_agent()
