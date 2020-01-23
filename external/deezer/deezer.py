import requests
from flask import abort


def create_search_request(artist, track):
    try:
        data = {
            "q":{
                "artist":artist,
                "track":track
            }
        }
        response = requests.get("https://api.deezer.com/search", data)
        if 'error' in response.json():
            return response.json()['error']['message']
        else:
            resp = response.json()['data'][0]
            return {
                "song_name": resp['title'],
                "album": resp['album']['title'],
                "image": resp['album']['cover_medium'],
                "duration": resp['duration'],
                "rank": resp['rank'],
                "album_id": resp['album']['id'],
                "song_id": resp['id'],
                "author": resp['artist']['name']
            }
    except:
        return "error request is wrong"
