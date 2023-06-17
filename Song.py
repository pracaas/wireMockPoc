import requests as requests


def add_song(url=None, body=None):
    if url is None:
        url = "http://localhost:8000/add-songs"
    response = requests.post(url=url, json=body)
    print(response.status_code)
    print(response.text)
    return response


if __name__ == "__main__":
    add_song(None, {"song_name": "enter sad ma"})
