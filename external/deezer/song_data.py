class SongData:
    album_id: int
    song_id: int
    name: str
    album: str
    image: str
    duration: int
    rank: int
    author: str

    def __init__(self, album_id, song_id, name, album, image, duration, rank, author):
        self.album_id = album_id
        self.song_id = song_id
        self.name = name
        self.album = album
        self.image = image
        self.duration = duration
        self.rank = rank
        self.author = author

    def to_dict(self):
        return {
            'album_id': self.album_id,
            'song_id': self.song_id,
            'name': self.name,
            'album': self.album,
            'image': self.image,
            'duration': self.duration,
            'rank': self.rank,
            'author': self.author,
        }
