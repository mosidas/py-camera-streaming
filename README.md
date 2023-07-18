# py-streaming-server

- https://blog.miguelgrinberg.com/post/video-streaming-with-flask
- https://leico.github.io/TechnicalNote/Linux/avconv-hls-webcam
- https://6715.jp/posts/20/
- https://zenn.dev/nkte8/articles/2021-10-12-r01


```bash
# execute in cmd.exe (not powershell)
cd static
python ../frame2stdout.py | ffmpeg -r 30 -i - -f hls -c:v libx264 -acodec libfaac -strftime 1 -strftime_mkdir 1 -hls_time 5 -hls_segment_filename %Y-%m-%d/v%H%M%S.ts -movflags faststart output.m3u8
```

```bash
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
$env:FLASK_APP = "server.py"
$env:FLASK_DEBUG=1
flask run
```