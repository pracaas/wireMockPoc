import httpretty
import requests

# Enable HTTPretty to intercept HTTP requests
httpretty.enable()

# Define the mock response
mock_response = {
    "status": 200,
    "body": '{"message": "Mocked response"}',
    "headers": {
        "Content-Type": "application/json"
    }
}

# Register the mock response for a specific URL
httpretty.register_uri(
    method=httpretty.GET,
    uri="http://api.example.com/some-endpoint",
    body=mock_response["body"],
    status=mock_response["status"],
    content_type=mock_response["headers"]["Content-Type"]
)

# Make an HTTP request to the mocked endpoint
response = requests.get("http://api.example.com/some-endpoints")

# Validate the response
assert response.status_code == mock_response["status"]
assert response.json()["message"] == "Mocked response"

# Disable HTTPretty
httpretty.disable()
httpretty.reset()
