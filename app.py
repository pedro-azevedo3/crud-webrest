import flask
from flask import request

from app.controllers.routers import healthcheck
from app.services.player import (create as create_player, delete as delete_player, list as list_player, get as get_player, patch as patch_player )
from app.services.club import (create, delete, list, get, patch)

app = flask.Flask(__name__)

#Player
@app.route('/',methods=['GET'])
def healthcheck():
    healthcheck()

@app.route('/players', methods=['POST'])
def save_player():
    return create_player(flask.request)

@app.route('/players/<int:id>', methods=['DELETE'])
def delete_player(id):
    return delete_player(id)

@app.route('/players', methods=['GET'])
def list_player():
    return list_player(flask.request)

@app.route('/players/<int:id>', methods=['GET'])
def get_player_by_id(id):
    return get_player(id)

@app.route('/players/<int:id>', methods=['PATCH'])
def update_player_by_id(id):
    return patch_player(id, flask.request)

#Club
@app.route('/clubs', methods=['POST'])
def save_club():
    return create(flask.request)

@app.route('/clubs/<int:id>', methods=['DELETE'])
def delete_club(id):
    return delete(id)

@app.route('/clubs', methods=['GET'])
def list_club():
    return list(flask.request)

@app.route('/clubs/<int:id>', methods=['GET'])
def get_club_by_id(id):
    return get(id)

@app.route('/clubs/<int:id>', methods=['PATCH'])
def update_club_by_id(id):
    return patch(id, flask.request)

if __name__ == "__main__":
    app.run(port=8080, debug=False)