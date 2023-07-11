from camera import VideoCamera
import sys

if __name__ == "__main__":
    cap = VideoCamera(0)

    fail_count = 0
    while True:
        jpeg = cap.get_frame()
        if not jpeg is None:
            sys.stdout.buffer.write(jpeg.tobytes())
            fail_count = 0
        else:
            fail_count = fail_count + 1
            if fail_count >= 60:
                sys.exit(1)
    cap = None
