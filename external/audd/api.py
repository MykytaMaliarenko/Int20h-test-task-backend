import os
import time

import requests
from .recognition_result import RecognitionResult


def search_by_lyrics(lyrics):
    data = {
        'api_token': os.environ["audd_api_token"],
        'method':   'findLyrics',
        'q':        lyrics
    }

    result = requests.post('https://api.audd.io/', data=data).json()
    if 'result' not in result:
        return None

    result = result['result']
    if len(result) == 0:
        return None

    return RecognitionResult(
        artist=result[0]['artist'],
        song=result[0]['title']
    )


def search_by_piece(path: str):
    data = {
        'api_token': os.environ["audd_api_token"],
        'method': 'recognizeWithOffset',
        'url': '{}/sound/{}'.format(os.environ["self_url"], path)
    }

    result = requests.post('https://api.audd.io/', data=data).json()
    if 'result' not in result:
        return None

    result = result['result']
    if len(result) == 0:
        return None

    return RecognitionResult(
        artist=result[0]['artist'],
        song=result[0]['title']
    )
