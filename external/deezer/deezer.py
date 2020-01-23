import requests
from flask import abort


def create_search_request(artist, track):
    try:
        search = "https://api.deezer.com/search?q=artist:%22{0}%22%20track:%22{1}%22".format(artist, track)
        response = requests.get(search)
        for key in response.json():
            if key == 'error':
                abort(500)
                print(response.json())
                break
        else:
            resp = response.json()['data'][0]
            data = {
                "song_name": resp['title'],
                "album": resp['album']['title'],
                "image": resp['album']['cover_medium'],
                "duration": resp['duration'],
                "rank": resp['rank'],
                "album_id": resp['album']['id'],
                "song_id": resp['id'],
                "author": resp['artist']['name']
            }
            return data

    except:
        abort(500)
