import requests


def get_token(app_id, redirect_uri, secret):
    data_for_authenticate = {
        "app_id": app_id,
        "redirect_uri": redirect_uri,
        "perms": "basic_access,email"
    }
    url_for_authenticate = "https://connect.deezer.com/oauth/auth.php"
    response = requests.head(url_for_authenticate, data_for_authenticate)
    response = response.json()
    data_for_getting_token = {
        "app_id": app_id,
        "secret": secret,
        "code": response['code']
    }
    url_for_getting_token = "https://connect.deezer.com/oauth/access_token.php"
    token = requests.get(url_for_getting_token, data_for_getting_token).json()
    return token['access_token']


def get_song_data(artist, track, token):
    data = {
        "access_token": token,
        "q": {
            "artist": artist,
            "track": track
        }
    }
    response = requests.get("https://api.deezer.com/search", data)
    if 'error' in response.json():
        return response.json()['error']['message']
    else:
        response = response.json()['data'][0]
        return {
            "song_name": response['title'],
            "album": response['album']['title'],
            "image": response['album']['cover_medium'],
            "duration": response['duration'],
            "rank": response['rank'],
            "album_id": response['album']['id'],
            "song_id": response['id'],
            "author": response['artist']['name']
        }
