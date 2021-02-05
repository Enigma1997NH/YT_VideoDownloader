#Function for Downloading Video

# BY : Enigma1997NH


from pytube import YouTube
def link(lin):
    Save_Path = "path"
    yt = YouTube(lin)
    print(yt.title)
    try:
        stream = yt.streams.first()
        stream.download(Save_Path)
    except:
        print("SOME ERROR!!...")
    print("DONE")



