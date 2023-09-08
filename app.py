import flask

app = flask.Flask(__name__)

@app.route('/',methods=['GET'])
def healthcheck():
    return 'WORKING'


if __name__ == "__main__":
    app.run(port=8080, debug=False)