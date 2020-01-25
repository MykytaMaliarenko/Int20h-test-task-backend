from flask_restful import Resource, reqparse , abort
from external.deezer import api as deezer_api
from external.audd import api as audd_api


parser = reqparse.RequestParser()
parser.add_argument('type', type=str, location='form')
parser.add_argument('data', location='form')


class GuessMusic(Resource):

    def get(self):
        args = parser.parse_args()
        type_ = args["type"]
        data = args["data"]
        try:
            if type_.upper() == "LYRICS":
                response = audd_api.search_by_lyrics(data)
            elif type_.upper() == "HUMMING":
                response = audd_api.search_by_piece(data)
        except KeyError:
            abort(500)
        return deezer_api.get_song_data(response.artist, response.song)



