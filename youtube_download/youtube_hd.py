from pytube import YouTube
import os


def youtube_hd(video_url, path):
    yt = YouTube(video_url)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    print(yt)
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)


youtube_hd('https://youtu.be/qmEXHa-53qg', '/home/diego/Vídeos')
