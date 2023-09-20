import os
import re
import time
import moviepy.editor as mp

from pytube import YouTube


def youtube():

    link = input("Write the link of the video you want to download\n")
    path = '/home/diego/Músicas'
    yt = YouTube(link)

    st = time.time()
    print("Downloading...")
    ys = yt.streams.filter(only_audio=True).first().download(path)
    print("Download complete")
    et = time.time()

    final_time_downloading = et - st
    print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(final_time_downloading)))

    print("Converting file...")
    st_converting = time.time()
    for file in os.listdir(path):
        if re.search('mp4', file):
            mp4_path = os.path.join(path, file)
            mp3_path = os.path.join(path, os.path.splitext(file)[0] + '.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)

    et = time.time()
    final_time_converting = et - st
    print('Conversion time from mp4 to mp3:', time.strftime("%H:%M:%S", time.gmtime(final_time_converting)))
    print('Successful!')


if __name__ == '__main__':
    youtube()
