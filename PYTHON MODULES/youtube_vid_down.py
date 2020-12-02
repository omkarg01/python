# importing module
import youtube_dl

ydl_opts = {}

def dwl_vid():
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([zxt])

channel = 1
while (channel == int(1)):
	link_of_the_video = input("https://www.youtube.com/watch?v=sa-TUpSx1JA&t=49s")
	zxt = link_of_the_video.strip()

	dwl_vid()
	channel = int(input(0))
