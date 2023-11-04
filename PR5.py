import pytube

# Ссылка на видео.
link = "https://www.youtube.com/watch?v=ciT_61atIS4" 
# Место сохранения.
path = "/home/korens/py"

YT_parser = pytube.YouTube(link)

video_with_highest_resolution = YT_parser.streams.get_highest_resolution()
video_with_highest_resolution.download(path)