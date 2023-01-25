from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
import requests
import json


app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/proxy")
@cross_origin(support_credentials=True)
def proxy():
    url = request.args.get("url")
    if not url:
        return "Error: No URL provided.", 400

    try:
        response = requests.get(url)
        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        return "Error: {}".format(e), 500


if __name__ == "__main__":
    app.run()
