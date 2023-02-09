from pytube import Playlist,YouTube

playlist = Playlist('https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n')
print('Number of videos in playlist: %s' % len(playlist.video_urls))

for items in playlist.video_urls:
    link = str(items)
    yt = YouTube(link)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    print('Video Download')
