import json
import os
import handlers
from flask import Flask
from flask_restful import Api

ENV_FILE = "env.json"

app = Flask(__name__)
api = Api(app)

handlers.init(api)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


def init_env():
    if os.path.isfile(ENV_FILE):
        with open(ENV_FILE, "r") as file:
            data = json.load(file)
            for key in data:
                os.environ[key] = data[key]


if __name__ == '__main__':
    init_env()
    app.run(debug=True)
