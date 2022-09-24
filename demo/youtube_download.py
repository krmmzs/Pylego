#!/usr/bin python3

from pytube import YouTube
import os

# url input from user.
yt = YouTube("https://www.youtube.com/watch?v=VYQVlVoWoPY").streams.first().download()

# extract only audio.
video = yt.streams.filter(only_audio=True).first()

# check for destination to save file.
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or "."

# download the file.
out_file = video.download(output_path=destination)

# save the file.
# works but it's a bad practice: youtube is basic in mp4 format, just changing the file extension
# to .mp3 is not enough.
base, ext = os.path.splitext(out_file)
new_file = base + ".mp3"
os.rename(out_file, new_file)

# result of success.
print(yt.title + " has been successfully downloaded in .mp3 format.")
