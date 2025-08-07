from google.adk.agents import Agent, SequentialAgent
from google.adk.tools import FunctionTool
import urllib.request

# Define a maximum character length to avoid sending too much data to the model.
MAX_CONTENT_LENGTH = 16000

def fetch_url_content(url: str) -> str:
    """Fetches and returns the text content of a given URL, truncated to a max length.

    Args:
        url: The URL to fetch the content from.

    Returns:
        The text content of the URL, truncated if necessary.
    """
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            if len(content) > MAX_CONTENT_LENGTH:
                content = content[:MAX_CONTENT_LENGTH] + "\n[... content truncated ...]"
            return content
    except Exception as e:
        return f"An error occurred: {e}"

# Wrap the function as a FunctionTool
url_fetch_tool = FunctionTool(fetch_url_content)

# Define the first task: fetching content from a URL
fetching_agent = Agent(
    name="FetchingAgent",
    model="gemini-1.5-flash",
    description="An agent that fetches content from a URL.",
    instruction='You are an agent that fetches content from a URL. Your only job is to call the `url_fetch_tool` with the given URL and output the raw, unmodified text content returned by the tool. Do not add any explanation or summary.',
    tools=[url_fetch_tool]
)

# Define the second task: summarizing the fetched content
summarizing_agent = Agent(
    name="SummarizingAgent",
    model="gemini-1.5-flash",
    description="Summarizing Agent",
    instruction='Summarize the input text which is the content of a blog post.',
)

# Define the sequential pipeline
blog_pipeline_agent = SequentialAgent(
    name="blog_pipeline_agent",
    sub_agents=[fetching_agent, summarizing_agent],
    description="A pipeline agent that fetches content from a blog URL and summarizes it.",
)

root_agent = blog_pipeline_agent