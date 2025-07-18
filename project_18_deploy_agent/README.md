# Project 18: Cloud Run Deployment Example

**HERE AND NOW AI**

*designed with passion for innovation*

---

## Project Description

This project provides a basic example of how to package an ADK agent for deployment as a web service using Docker and Google Cloud Run. The agent is a simple "greeter" that responds to HTTP requests. This is a starting point for building scalable and production-ready ADK applications.

## Usage Instructions

1.  **Install Docker:**

    Follow the instructions on the [Docker website](https://docs.docker.com/get-docker/) to install Docker on your machine.

2.  **Build the Docker image:**

    ```bash
    docker build -t adk-greeter-agent .
    ```

3.  **Run the Docker container locally:**

    ```bash
    docker run -p 8080:8080 adk-greeter-agent
    ```

4.  **Test the agent:**

    Open a new terminal and send a request to the agent:

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"message": "Hello"}' http://localhost:8080/
    ```

5.  **Deploy to Cloud Run:**

    Follow the [Google Cloud Run documentation](https://cloud.google.com/run/docs/deploying) to deploy the container image to Cloud Run.

---

**HERE AND NOW AI** | [Website](https://hereandnowai.com) | [Contact](mailto:info@hereandnowai.com)

*Logo: ![[Logo]](https://raw.githubusercontent.com/hereandnowai/images/refs/heads/main/logos/HNAI%20Title%20-Teal%20%26%20Golden%20Logo%20-%20DESIGN%203%20-%20Raj-07.png)*