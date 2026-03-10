from flask import Flask, request, send_file
import yt_dlp
import uuid
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Blackfyre API running"

@app.route("/download")
def download():

    url = request.args.get("url")

    if not url:
        return "Missing video URL"

    filename = str(uuid.uuid4()) + ".mp4"

    ydl_opts = {
        'format': 'best',
        'outtmpl': filename
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return send_file(filename, as_attachment=True)

    except Exception as e:
        return str(e)

    finally:
        if os.path.exists(filename):
            os.remove(filename)

app.run(host="0.0.0.0", port=10000)

