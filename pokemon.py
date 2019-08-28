from flask import Flask, send_from_directory, request, abort, jsonify, render_template, url_for, redirect
import os
import requests
import json
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('pokemon.html')

@app.route('/hasil', methods=['POST'])
def pokemon():
    if request.method == 'POST':
        nama = request.form['nama']
        url = 'https://pokeapi.co/api/v2/pokemon/' + nama
        ambil = (requests.get(url))
        try:
            ambil.json()
        except json.decoder.JSONDecodeError:
            return render_template('err.html')
        else:
            name = ambil.json()['name']
            height = ambil.json()['height']
            weight = ambil.json()['weight']
            img = ambil.json()['sprites']["front_default"]
            return render_template('hasilpokemon.html', data = {'name': name, 'height': height, 'weight': weight, 'img': img})
    else:
        return render_template('err.html')
       
@app.errorhandler(404)
def notFound(error):
    return render_template('err.html')

if __name__ == '__main__':
    app.run(
        debug = True,
        host = '0.0.0.0',
        port = 1234
    )