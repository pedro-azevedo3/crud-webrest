import flask
from flask import request

from app.controllers.routers import healthcheck
from app.services.pdfs import create

app = flask.Flask(__name__)

@app.route('/',methods=['GET'])
def healthcheck():
    healthcheck()

@app.route('/pdfs', methods=['POST'])
def save_pdf():
    return create(flask.request)

if __name__ == "__main__":
    app.run(port=8080, debug=False)