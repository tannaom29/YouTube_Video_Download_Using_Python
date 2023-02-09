from pytube import YouTube

link = str(input('Youtube Video URL'))

yt = YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()
print('Video Download')