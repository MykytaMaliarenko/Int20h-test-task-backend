import time
import werkzeug
from flask_restful import Resource, reqparse , abort
from external.deezer import api as deezer_api
from external.audd import api as audd_api


parser = reqparse.RequestParser()
parser.add_argument('type', type=str, location='form')


class GuessMusic(Resource):
    def post(self):
        args = parser.parse_args()
        type_ = str(args["type"])
        data = None

        if type_.lower() == "lyrics":
            parser.add_argument('data', type=str, location='form')
            data = str(parser.parse_args()['data'])
        elif type_.lower() == "humming":
            parser.add_argument('data', type=werkzeug.datastructures.FileStorage, location='files')
            args = parser.parse_args()
            data = args['data']
            data.save("sound/{}".format(str(int(round(time.time() * 1000)))))
            data = "sound/{}".format(str(int(round(time.time() * 1000))))

        if data is None:
            abort(400, msg="unknown type")

        try:
            if type_.lower() == "lyrics":
                response = audd_api.search_by_lyrics(data)
            elif type_.lower() == "humming":
                response = audd_api.search_by_piece(data)
        except KeyError:
            abort(500)

        if response is None:
            abort(404, msg="couldn't recognise")
        else:
            deezer_response = deezer_api.get_song_data(response.artist, response.song)
            if deezer_response is None:
                abort(404, msg="couldn't find info in deezer")
            else:
                return deezer_api.get_song_data(response.artist, response.song).to_dict()
