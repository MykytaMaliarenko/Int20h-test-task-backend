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
        artist=result['artist'],
        song=result['title']
    )


def search_by_piece(piece):
    data = {
        'api_token': os.environ["audd_api_token"],
        'method': 'recognizeWithOffset',
        'url':  'https://audd.tech/example_h1.ogg'
    }
    result = requests.post('https://api.audd.io/', data=data).json()['result']
    return RecognitionResult(
        artist=result['artist'],
        song=result['title']
    )
