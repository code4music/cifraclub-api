"""API Module"""

import os
from flask import Flask, json
from cifraclub import CifraClub

app = Flask(__name__)

@app.route('/')
def home():
    """Home route"""
    return app.response_class(
        response=json.dumps({'api': 'Cifra Club API'}),
        status=200,
        mimetype='application/json'
    )

@app.route('/artists/<artist>/songs/<song>')
def get_cifra(artist, song):
    """Get cifra by artist and song"""
    cifrablub = CifraClub()
    return app.response_class(
        response=json.dumps(cifrablub.cifra(artist, song), ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT', '3000'), debug=True)
