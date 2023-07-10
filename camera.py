import datetime
import subprocess
import threading
import time
import cv2
import numpy as np
import re
import logging
import traceback

tsl = []
seq = 0


def live():
    threading.Thread(target=__live).start()


def __live():
    global seq
    while True:
        try:
            filename = create_mp4()
            playlist = encode_ts(filename)
            tsl.extend(playlist)
            # time.sleep(float(tsl[0][0]))
            # tsl.pop(0)
            seq += 1
        except:
            logging.exception(traceback.format_exc())
            pass


def create_mp4(duration=5):
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # fps
    fps = int(camera.get(cv2.CAP_PROP_FPS))
    # width
    w = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    # height
    h = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # fourcc
    fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
    # filename
    filename = datetime.datetime.now().strftime("static/%Y%m%d_%H%M%S") + ".mp4"
    # create the video.
    video = cv2.VideoWriter(filename, fourcc, fps, (w, h))

    # start recording.
    start_time = time.time()
    while True:
        ret, frame = camera.read()
        if ret == False:
            break

        # save the frame.
        video.write(frame)

        # Stop recording after the duration.
        if time.time() - start_time > duration:
            break

    # release the camera.
    camera.release()
    cv2.destroyAllWindows()

    return filename


def encode_ts(filename):
    command = [
        # TODO: Change the path.
        "C:/apps/ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe",
        "-i",
        filename,
        "-f",
        "hls",
        "-c:v",
        "libx264",
        "-acodec",
        "libfaac",
        "-hls_time",
        "5",
        "-hls_list_size",
        "0",
        "-start_number",
        str(int(time.time() * 1000)),
        "-hls_segment_filename",
        "static/h_%d.ts",
        "pipe:1",
    ]
    data = subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, shell=True
    )

    playlist = data.stdout.decode("utf-8")
    playlist = playlist[playlist.rfind("#EXTM3U") :]
    return re.findall(r"#EXTINF:([\d.]+),\s+(\S+)", playlist)


def get_playlist():
    global seq
    pl = [
        "#EXTM3U",
        "#EXT-X-VERSION:3",
        "#EXT-X-TARGETDURATION:6",
        "#EXT-X-MEDIA-SEQUENCE:%d" % seq,
    ]

    for ts in tsl:
        pl.append("#EXTINF:%s," % ts[0])
        pl.append("#EXT-X-DISCONTINUITY")
        pl.append("/static/%s" % ts[1])

    return "\n".join(pl)


if __name__ == "__main__":
    while True:
        try:
            filename = create_mp4()
            playlist = encode_ts(filename)
            tsl.extend(playlist)
            # time.sleep(float(tsl[0][0]))
            # tsl.pop(0)
            seq += 1
        except KeyboardInterrupt:
            print("Close.")
            break
        except:
            logging.exception(traceback.format_exc())
            pass
