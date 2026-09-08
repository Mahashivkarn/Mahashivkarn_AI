#This file looks for folder in ures_upload folder and convert in into audio and video.
import os

def text_to_audio(folder):
    print("TTA - ",folder)

def create_reel(folder):
    print("TTR - " ,folder)
    

if __name__ == "__main__":
    with open("done.txt","r") as f:
        done_folders =f.readlines()
    
           
        done_folders =[f.strip() for f in done_folders ]
        
        folders = os.listdir("user_uploads")
        print(folders,done_folders)
        for folder in folders:
            if (folder not in done_folders):
                text_to_audio(folder)#Genertae the audio.mp3 from desc.txt
                create_reel(folder)#Convert the images and audio mp3 inside the folder to reel.
                
                with open("done.txt","a") as f:
                    f.write(folder + "\n")