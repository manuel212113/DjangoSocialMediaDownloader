from django.shortcuts import render,redirect
import numpy as np

from pytube import YouTube

def HomePage(request):
    return render(request,'views/index.html')



def YoutubeConverter(request):
    return render(request,'views/index.html')


def GetVideoYoutube(request,videoId):
    videoId='https://youtu.be/'+videoId
    Video=YouTube(videoId)
    DownloadVideo=Video.streams
    
    
    print(DownloadVideo.filter(res="720p"))

    
    
    return render(request,'views/index.html',{'video': Video.title, 'image':Video.thumbnail_url,'description':Video.description, 'Download':DownloadVideo   })