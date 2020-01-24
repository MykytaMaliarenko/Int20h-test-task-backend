import os
import requests
from .recognition_result import RecognitionResult


def search_by_lyrics(lyrics):
    data = {
        'api_token': os.environ["audd_api_token"],
        'method':   'findLyrics',
        'q':        lyrics
    }
    result = requests.post('https://api.audd.io/', data=data).json()['result']
    return RecognitionResult(
        artist=result[0]['artist'],
        song=result[0]['title']
    )


def search_by_piece(piece):
    with open("sound/{}".format(len(piece)), "w") as f:
        f.write(piece)

    data = {
        'api_token': os.environ["audd_api_token"],
        'method': 'recognizeWithOffset',
        'url': '{}/sound/{}'.format(os.environ["self_url"], len(piece))
    }
    result = requests.post('https://api.audd.io/', data=data).json()['result']
    return RecognitionResult(
        artist=result[0]['artist'],
        song=result[0]['title']
    )
