from camera import VideoCamera
import sys


if __name__ == "__main__":
    cap = VideoCamera(0)
    if cap.isOpened() == False:
        sys.exit(1)

    fps = cap.get_fps()
    if fps is None:
        sys.exit(1)

    print(f"CAMERA_FPS={str(fps)}")
    print(f"KEYINT_MIN={str(fps * 5)}")
