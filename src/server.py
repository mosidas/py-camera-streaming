from flask import Flask, render_template, Response, send_file
import flask
import camera
import hls
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("werkzeug")
log.info("Starting server...")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
