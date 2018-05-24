header = {
    "cellTowers": [
        {
            "cellId": 42,
            "locationAreaCode": 415,
            "mobileCountryCode": 310,
            "mobileNetworkCode": 410,
            "age": 0,
            "signalStrength": -60,
            "timingAdvance": 15
        }
    ]
}


from pytube import YouTube


play_list = 'https://www.youtube.com/playlist?list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_';

yt = YouTube(play_list)
yt = yt.get('mp4', '720p')
yt.download('/home/uzzal/Downloads')
