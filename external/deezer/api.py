from external.deezer.song_data import SongData
import requests
import os


def get_song_data(artist: str, song: str) -> SongData:
    data = {
        "access_token":os.environ['deezer_token'],
        "q": "artist:'{}'track:'{}'".format(artist, song)
    }
    response = requests.get("https://api.deezer.com/search", data)
    if 'error' in response.json():
        raise ValueError("The request isn't correct")
    else:
        if len(response.json()['data']) == 0:
            return None
        else:
            response = response.json()['data'][0]
            return SongData(
                name=response['title'],
                album=response['album']['title'],
                image=str(response['album']['cover_medium']).replace("250x250", "150x150"),
                duration=int(response['duration']),
                rank=int(response['rank']),
                album_id=int(response['album']['id']),
                song_id=int(response['id']),
                author=response['artist']['name']
            )

