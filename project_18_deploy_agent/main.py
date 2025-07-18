
import adk
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Create a simple greeter agent
agent = adk.Agent(instructions="You are a friendly greeter.")
runner = adk.Runner()

class AgentRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            request_data = json.loads(post_data)

            # Run the agent with the message from the request
            output = runner.run(agent, request_data['message'])

            # Send the response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"response": output}).encode('utf-8'))

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))

def run_server():
    """Runs the agent as an HTTP server."""
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, AgentRequestHandler)
    print("Starting server on port 8080...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
