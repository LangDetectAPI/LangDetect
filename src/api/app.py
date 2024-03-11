from typing import Optional, Dict

from flask import Flask, Response, request
import json
from langDetect import LangDetect, langs

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_infos():
    # Votre code ici

    # Convertir le dictionnaire en JSON
    json_data = json.dumps(langs)

    # Créer une réponse avec le JSON et le Content-Type défini sur application/json
    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )

    return response


@app.route("/detect", methods=["POST"])
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
    app.run(debug=True, port=8080)
