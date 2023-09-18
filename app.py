import flask
from flask import request

from app.controllers.routers import healthcheck
from app.services.pdfs import (create, delete, list, get, patch)

app = flask.Flask(__name__)

@app.route('/',methods=['GET'])
def healthcheck():
    healthcheck()

@app.route('/pdfs', methods=['POST'])
def save_pdf():
    return create(flask.request)

@app.route('/pdfs/<int:id>', methods=['DELETE'])
def delete_pdf(id):
    return  delete(id)

@app.route('/pdfs', methods=['GET'])
def list_pdf():
    return list(flask.request)

@app.route('/pdfs/<int:id>', methods=['GET'])
def get_by_id(id):
    return get(id)

@app.route('/pdfs/<int:id>', methods=['PATCH'])
def update_by_id(id):
    return patch(id, flask.request)

if __name__ == "__main__":
    app.run(port=8080, debug=False)