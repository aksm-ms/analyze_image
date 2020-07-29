import json

from image_details import get_image_details
from db import write_to_db

from flask import Flask, request

app = Flask(__name__)


@app.route("/analyze", methods=['POST'])
def analyze():
    print("POST call for analyzing image")
    print("request.files:" + str(request.files['file']))

    response = get_image_details(request.files['file'])
    print("response: " + json.dumps(response))

    write_to_db(response)
    return response


@app.route("/")
def print_msg():
    return "Flask app running..."


if __name__ == '__main__':
    app.run()
