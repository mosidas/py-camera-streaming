from flask import Flask, render_template, Response, send_file
import camera
import hls
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)

log.info("Starting server...")
app = Flask(__name__)
# run hls function in background.


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/camera_strem")
def streming():
    return Response(
        camera.streming(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


# TODO: This function is not working.
@app.route("/hls_stream")
def hls_streaming():
    # send the m3u8 file.
    return send_file("hls/h.m3u8")
