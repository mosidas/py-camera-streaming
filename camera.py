import datetime
import time
import cv2
import numpy as np


def streming():
    """
    This function is used to stream the video from the camera.
    yield returns the frame jpg file of the video.
    """
    video = cv2.VideoCapture(0)
    title = "Video"
    while True:
        try:
            ok, frame = video.read()
            if ok == True:
                # Resize to fit display frame.
                resized_frame = cv2.resize(frame, (500, 500))

                # add date to the frame.
                cv2.putText(
                    img=resized_frame,
                    # format: "Date: 2020-01-01 00:00:00"
                    text="Date:"
                    + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    org=(5, 20),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.5,
                    color=(0, 255, 0),
                    thickness=2,
                    lineType=cv2.LINE_AA,
                )

                # Convert jpg file.
                ok, jpg = cv2.imencode(".jpg", resized_frame)

                frame = jpg.tobytes()

                # Yield the frame in byte format.
                yield b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
            else:
                # return the white frame.
                size = (500, 500)
                black_img = np.zeros(size, np.uint8)
                white_img = black_img + 255
                frame = white_img.tobytes()
                yield b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
                print("Camera is not available.")

            cv2.waitKey(1)

        except KeyboardInterrupt:
            # Press '[ctrl] + [c]' on the console to exit the program.
            print("Close.")
            break

    video.release()
    cv2.destroyAllWindows()
