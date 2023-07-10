import datetime
import time
import cv2
import numpy as np


def save_movie(duration=10):
    """
    This function is used to save the video from the camera.
    duration: int
        The duration of the video.(sec)
    """

    # get the camera.
    camera = cv2.VideoCapture(0)
    # config for saving the video.
    # fps
    fps = int(camera.get(cv2.CAP_PROP_FPS))
    # width
    w = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    # height
    h = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # fourcc
    fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
    # filename
    filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".mp4"
    # create the video.
    video = cv2.VideoWriter(filename, fourcc, fps, (w, h))

    # start recording.
    start_time = time.time()
    while True:
        ret, frame = camera.read()
        if ret == False:
            break

        # show the frame.
        cv2.imshow("camera", frame)
        # save the frame.
        video.write(frame)

        # Press 'q' to exit the program.
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        # Stop recording after the duration.
        if time.time() - start_time > duration:
            break

    # release the camera.
    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    save_movie()
