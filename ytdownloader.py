from pytube import YouTube
from sys import argv

link = input("What is the URL you want to download?")

choice = input('Enter 1 to download audio only or 2 for video: ')

if choice == '1':
    yt = YouTube(link)
    yd = yt.streams.get_audio_only()
else:
    yt = YouTube(link)
    yd = yt.streams.get_highest_resolution()

yd.download('target folder here')
