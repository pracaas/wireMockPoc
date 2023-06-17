import unittest
from Song import add_song
import httpretty

def stub():
    # Enable HTTPretty to intercept HTTP requests
    httpretty.enable()

    # Define the mock response
    mock_response = {
        "status": 200,
        "body": 'The Return',
        "headers": {
            "Content-Type": "application/json"
        }
    }

    # Register the mock response for a specific URL
    httpretty.register_uri(
        method=httpretty.POST,
        uri="http://localhost:8084/add-songs",
        body=mock_response["body"],
        status=mock_response["status"],
        content_type=mock_response["headers"]["Content-Type"]
    )


class TestPlayList(unittest.TestCase):



    def test_should_return_song_name(self):
        # given
        song = {"song_name": "The Return"}
        stub()

        # when
        response = add_song("http://localhost:8084/add-songs", song)

        # then
        httpretty.reset()
        self.assertIsNotNone(response)
        self.assertEqual(200, response.status_code)
        self.assertEqual("The Return", response.text)
