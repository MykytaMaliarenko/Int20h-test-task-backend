from flask_restful import Api
from handlers.audd_api_recognition import AuddApiRecognition


def init(api: Api):
    api.add_resource(AuddApiRecognition, "/sound/<int:file_id>")
