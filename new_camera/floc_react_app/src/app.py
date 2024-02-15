from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/test", methods=["GET"])
def hello_world():
    return {"message": "Hello, World from Flask!"}


@app.route("/upload", methods=["POST"])
def upload_image():

    return {"message": "Image uploaded"}


if __name__ == "__main__":
    app.run(debug=True)
