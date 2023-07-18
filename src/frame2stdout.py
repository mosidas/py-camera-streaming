from camera import VideoCamera
import sys

if __name__ == "__main__":
    cap = VideoCamera(0)

    fail_count = 0
    while True:
        ok, frame = cap.get_frame()
        if ok:
            sys.stdout.buffer.write(frame.tobytes())
            fail_count = 0
        else:
            fail_count = fail_count + 1
            if fail_count >= 60:
                sys.exit(1)
    cap = None
