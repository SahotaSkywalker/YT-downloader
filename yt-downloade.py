from email.mime import audio
from youtube_dl import YoutubeDL

audio = YoutubeDL({
    'format':'bestaudio'
})

video = YoutubeDL({
    'format':'mp4'
})



def Audio():
    
    url = input("Enter url of video: ")
    audio.extract_info(url)
        

def Video():
    url = input("enter url of video mp4: ")
    video.extract_info(url)


        


if __name__ == "__main__":
    while True:
        print("Choose what do u want to download from youTube")
        print("1.Audio\n2.Video")
        option = int(input("choose your option: "))
        if option ==1:
            Audio()
        elif option ==2:
            Video()
        
        con = input("do you want to continue(y/n): ")
        if con != "y":
            break