import flask
import healthcheck from app.api.routers

app = flask.Flask(__name__)

@app.route('/',methods=['GET'])
healthcheck()

if __name__ == "__main__":
    app.run(port=8080, debug=False)