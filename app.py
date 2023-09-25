import flask
from flask import request

from app.controllers.routers import healthcheck
from app.services.player import (create, delete, list, get, patch)

app = flask.Flask(__name__)

@app.route('/',methods=['GET'])
def healthcheck():
    healthcheck()

@app.route('/players', methods=['POST'])
def save_player():
    return create(flask.request)

@app.route('/players/<int:id>', methods=['DELETE'])
def delete_player(id):
    return delete(id)

@app.route('/players', methods=['GET'])
def list_player():
    return list(flask.request)

@app.route('/players/<int:id>', methods=['GET'])
def get_player_by_id(id):
    return get(id)

@app.route('/players/<int:id>', methods=['PATCH'])
def update_player_by_id(id):
    return patch(id, flask.request)

if __name__ == "__main__":
    app.run(port=8080, debug=False)