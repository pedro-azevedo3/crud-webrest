import flask
from flask import request
from flask_cors import CORS
from pymongo import MongoClient

from app.controllers.routers import healthcheck
from app.services.player import (create_player, delete_player, list_player,get_player ,patch_player )
from app.services.club import (create, delete, list, get, patch)

app = flask.Flask(__name__)
cors = CORS(app)
client = MongoClient('mongodb://45.6.38.11:27017') #localhost:27017

#Player
@app.route('/',methods=['GET'])
def healthcheck():
    healthcheck()

@app.route('/players', methods=['POST'])
def save_player():
    return create_player(flask.request,client)

@app.route('/players/<id>', methods=['DELETE'])
def delete_player(id):
    return delete_player(id, client)

@app.route('/players', methods=['GET'])
def list_players():
    return list_player(flask.request, client)

@app.route('/players/<id>', methods=['GET'])
def get_player_by_id(id):
    return get_player(id, client)

@app.route('/players/<id>', methods=['PATCH'])
def update_player_by_id(id):
    return patch_player(id, flask.request, client)

#Club
@app.route('/clubs', methods=['POST'])
def save_club():
    return create(flask.request, client)

@app.route('/clubs/<id>', methods=['DELETE'])
def delete_club(id):
    return delete(id, client)

@app.route('/clubs', methods=['GET'])
def list_club():
    return list(flask.request, client)

@app.route('/clubs/<id>', methods=['GET'])
def get_club_by_id(id):
    return get(id, client)

@app.route('/clubs/<id>', methods=['PATCH'])
def update_club_by_id(id):
    return patch(id, flask.request, client)

if __name__ == "__main__":
    app.run(port=8080, debug=True)