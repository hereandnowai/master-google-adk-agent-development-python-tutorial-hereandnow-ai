# Project 27: Code Review Assistant

**HERE AND NOW AI**

*designed with passion for innovation*

---

## Project Description

This project demonstrates how to build a code review assistant. The agent will use the GitHub API to fetch code from a repository, analyze it (e.g., count lines, look for TODOs), and return a summary. This is an advanced example of how to build an agent that can automate development workflows.

## Usage Instructions

1.  **Install the necessary libraries:**

    ```bash
    pip install google-adk==0.1.0 PyGithub
    ```

2.  **Set up GitHub authentication:**

    You will need a GitHub personal access token. You can create one [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

3.  **Set the `GITHUB_TOKEN` environment variable:**

    ```bash
    export GITHUB_TOKEN="your_personal_access_token"
    ```

4.  **Run the script:**

    ```bash
    python project_27_code_reviewer.py
    ```

5.  **Interact with the agent:**

    When prompted, ask the agent to review a repository, for example:

    ```
    Review the repository "google/generative-ai-python"
    ```

4.  **Expected Output:**

    The agent will provide a code review summary, including the number of lines of code and any TODOs found.

---

**HERE AND NOW AI** | [Website](https://hereandnowai.com) | [Contact](mailto:info@hereandnowai.com)

*Logo: ![[Logo]](https://raw.githubusercontent.com/hereandnowai/images/refs/heads/main/logos/HNAI%20Title%20-Teal%20%26%20Golden%20Logo%20-%20DESIGN%203%20-%20Raj-07.png)*