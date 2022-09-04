from pytube import YouTube
from sys import argv

link = input("What is the URL you want to download?")

choice = input(
    'Enter \n 1 to download audio only \n 2 for video\n 3 for both\n: ')

if choice == '1':
    yt = YouTube(link)
    yda = yt.streams.get_audio_only()
    yda.download('/Users/folder/Documents/YT/audio')
elif choice == '2':
    yt = YouTube(link)
    ydv = yt.streams.get_highest_resolution()
    ydv.download('/Users/folder/Documents/YT/video')
else:
    yt = YouTube(link)
    yda = yt.streams.get_audio_only()
    ydv = yt.streams.get_highest_resolution()
    yda.download('/Users/folder/Documents/YT/audio')
    ydv.download('/Users/folder/Documents/YT/video')

# yd.download('/Users/NEJ/Documents/YT')
