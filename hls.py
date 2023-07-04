import cv2
import subprocess


def create_hls():
    command = [
        "ffmpeg",
        "-i",
        "input.mp4",
        "-codec",
        "copy",
        "-vbsf",
        "h264_mp4toannexb",
        "-map",
        "0",
        "-f",
        "segment",
        "-segment_format",
        "mpegts",
        "-segment_time",
        "5",
        "-segment_list",
        "hls/h.m3u8",
        "hls/h_%5d.ts",
    ]
    subprocess.run(command, stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
