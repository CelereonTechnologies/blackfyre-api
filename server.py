from flask import Flask, request, send_file
import yt_dlp
import uuid
import os

app = Flask(__name__)

@app.route("/download")
def download():

    url = request.args.get("url")

    filename=str(uuid.uuid4())+".mp4"

    ydl_opts = {
        'format': 'mp4',
        'outtmpl': filename
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    response=send_file(filename, as_attachment=True)

    os.remove(filename)

    return response

app.run(host="0.0.0.0", port=10000)