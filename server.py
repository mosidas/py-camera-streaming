from flask import Flask, render_template, Response, send_file
import flask
import camera
import hls
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)
log.info("Starting server...")

# run hls function in background.
camera.live()


@app.route("/")
def index():
    return render_template("index.html")


# @app.route("/camera_strem")
# def streming():
#     return Response(
#         camera.streming(), mimetype="multipart/x-mixed-replace; boundary=frame"
#     )


# TODO: This function is not working.
@app.route("/hls_stream")
def hls_streaming():
    return flask.Response(
        response=camera.get_playlist(), mimetype="application/x-mpegURL"
    )
