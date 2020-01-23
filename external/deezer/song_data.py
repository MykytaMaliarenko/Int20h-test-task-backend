from dataclasses import dataclass


@dataclass
class SongData:
    album_id: int
    song_id: int
    name: str
    album: str
    image: str
    duration: int
    rank: int
    author: str
