from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Song(BaseModel):
    song_name: str


@app.post(path="/add-songs")
def hello(song: Song):
    print("Song Name", song.song_name)
    return song.song_name

# if __name__ == "__main__":
