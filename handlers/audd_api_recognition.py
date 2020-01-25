import os
from flask_restful import Resource, abort


class AuddApiRecognition(Resource):

    def get(self, file_id: int):
        try:
            with open("audio/{}".format(file_id), "rb") as f:
                data = list(f.read())
            os.remove("audio/{}".format(file_id))
            return data, 200
        except FileNotFoundError or FileExistsError:
            abort(404, message="audio {} doesn't exist".format(file_id))
        except EOFError:
            abort(500)
