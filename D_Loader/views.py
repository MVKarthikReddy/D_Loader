from django.http import HttpResponse
from django.shortcuts import render

from pytube import YouTube
from pytube import Playlist




# To download youtube videos

def u_download(link):
    ls = {}
    # num = int(input("Enter \n1 - Download a single video \n2 - Download a playlist\n"))
    if(1):
        # link = input("enter the link : ")
        yt = YouTube(link)
        video = yt.streams.all()

        vd = list(enumerate(video))
        print(len(vd))
        for i in vd:
            print(i)
            

        strm = int(input("enter quality code : "))
        video[strm].download()
    else:
        link = input("enter the link : ")
        py = Playlist(link)
        print(f'Downloading : {py.title}')
        i=0
    
        for video in py.videos:
            # video.streams.first().download()
            print(video.streams[i])
            i+=1
    print("Succesfully downloaded")
    return dict(ls)












def home(request):
    return render(request,"index.html")
def getdata(request):
    a = u_download(request.GET.get("url","off"))
    params = {"name":"Karthik Reddy","nature":"bad boy"}
    return render(request,"quality.html",params)