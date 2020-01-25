from flask_restful import Api
from handlers.audd_api_recognition import AuddApiRecognition
from handlers.guess_music import GuessMusic


def init(api: Api):
    api.add_resource(AuddApiRecognition, "/sound/<int:file_id>")
    api.add_resource(GuessMusic, "/guessMusic")
