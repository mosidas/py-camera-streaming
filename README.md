# py-streaming-server

- https://blog.miguelgrinberg.com/post/video-streaming-with-flask
- https://leico.github.io/TechnicalNote/Linux/avconv-hls-webcam
- https://6715.jp/posts/20/


```powershell
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
$env:FLASK_APP = "server.py"
$env:FLASK_ENV = "development"
flask run
```