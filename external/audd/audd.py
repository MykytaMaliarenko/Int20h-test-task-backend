def search_by_lyrics(lyrics):
    data = {
        'api_token': os.environ["audd_api_token"],
        'method':   'findLyrics',
        'q':        lyrics
    }
    result = requests.post('https://api.audd.io/', data=data).json()['result']
    return {
        'artist': result['artist'],
        'title': result['title'],
        'album': result['album']
    }

def search_by_piece(piece):
    data = {
        'api_token': os.environ["audd_api_token"],
        'method': 'recognizeWithOffset',
        'url':  piece
    }
    result = requests.post('https://api.audd.io/', data=data).json()['result']
    return {
        'artist': result['artist'],
        'title': result['title'],
        'album': result['album']
    }

def search_by_piece_test(piece):
    piece = 'https://audd.tech/example_h1.ogg'
    data = {
        'api_token': os.environ["audd_api_token"],
        'method': 'recognizeWithOffset',
        'url':  piece
    }
    result = requests.post('https://api.audd.io/', data=data).json()['result']
    return {
        'artist': result['artist'],
        'title': result['title'],
        'album': result['album']
    }
