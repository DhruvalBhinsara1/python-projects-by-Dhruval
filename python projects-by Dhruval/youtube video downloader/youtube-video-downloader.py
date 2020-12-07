from pytube import YouTube
print("*YouTube Video Downloader*")
link = input("Past the video link:")
yt = YouTube(link)

videos = yt.streams.all()

i=1
for stream in videos:
    print(str(i)+""+str(stream))
    i+=1

stream_number = int (input("ENTER THE INDEX NUMBER:")) #number for the resolution. 


#NARUTO IS THE BEST ANIME EVER


video = videos[stream_number-1]

video.download('D:\songs')
print("downloaded")

