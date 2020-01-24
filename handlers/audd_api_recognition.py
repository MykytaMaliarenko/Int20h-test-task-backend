import os
from flask_restful import Resource, reqparse, abort

parser = reqparse.RequestParser()
parser.add_argument('id', type=int, location='args')


class AuddApiRecognition(Resource):

    def get(self, file_id: int):
        try:
            with open("audio/{}".format(file_id), "rb") as f:
                data = list(f.read())
            os.replace("audio/{}".format(file_id))
            return data, 200
        except FileNotFoundError or FileExistsError:
            abort(404, message="audio {} doesn't exist".format(file_id))
        except EOFError:
            abort(500)
