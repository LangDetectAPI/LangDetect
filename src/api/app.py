from flask import Flask, Response
import json

app = Flask(__name__)

@app.route("/detect/info", methods=["GET"])
def get_infos():
    # Votre code ici
    langs = {'eng': 'English', 'pol': 'Polish', 'deu': 'German', 'fra': 'French', 'spa': 'Spanish', 'ita': 'Italian', 'tur': 'Turkish', 
             'por': 'Portuguese', 'rus': 'Russian', 'ukr': 'Ukrainian', 'nld': 'Dutch', 'bul': 'Bulgarian', 'ell': 'Greek', 'swe': 'Swedish', 
             'hun': 'Hungarian', 'gle': 'Irish', 'lav': 'Latvian', 'dan': 'Danish', 'fin': 'Finnish',
             'ara': 'Arabic', 'heb': 'Hebrew', 'zho': 'Chinese', 'hin': 'Hindi', 'jpn': 'Japanese', 'fas': 'Persian', 'kor': 'Korean',
             'hye': 'Armenian', 'swa': 'Swahili', 'ber': 'Berber', 'kab': 'Kabyle', 'ces': 'Czech', 'lat': 'Latin',
             'nor': 'Norwegian', 'ron': 'Moldavian, Moldovan, Romanian', 'slk': 'Slovak', 'hbs': 'Serbo-Croatian', 'mkd': 'Macedonian'}

    # Convertir le dictionnaire en JSON
    json_data = json.dumps(langs)

    # Créer une réponse avec le JSON et le Content-Type défini sur application/json
    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )

    return response
