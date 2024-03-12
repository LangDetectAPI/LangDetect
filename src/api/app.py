from typing import Optional, Dict

from flask import Flask, Response, request
import json
from langDetect import LangDetect, langs


from flask import Blueprint


app = Flask(__name__)

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')

app.register_blueprint(api_v1)

@api_v1.route("/", methods=["GET"])
def get_infos():

    # Convertir le dictionnaire en JSON
    json_data = json.dumps(langs)

    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )

    return response


@api_v1.route("/detect", methods=["POST"])
def detect():
    data = request.get_json()
    text = data.get('text')

    if not text:
        return Response(response=json.dumps({'error': 'text is required'}), status=400, mimetype='application/json')

    print(text)

    predict = LangDetect().detect(text)

    json_data = json.dumps(predict)

    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )

    return response


if __name__ == "__main__":
    app.run(debug=True, port=5080)
