import os, sys 

def video_to_audio(video_file_path):
    
    if not os.path.isfile(video_file_path):
        sys.exit("ERROR! INCORRECT VIDEO FILE PATH")
        
    audio_file_path = video_file_path[:len(video_file_path)-4:] + "_extracted_audio.wav"
    
    # if file already exists
    if (os.path.isfile(audio_file_path)):
        return audio_file_path
    
    # -q:a 0 outputs audio with variable bitrate and the highest quality. 
    # -map 0:a selects all audio streams
    mp4_2_wav = "ffmpeg -i " + video_file_path + " -map 0:a -ab 8000 -ar 16000 -q:a 0 -vn " + audio_file_path + ""  # 16000 = 16kbps bit rate, 48000 = 48 kHz sampling rate

    os.system(mp4_2_wav)
    # -- END

    # CHECK IF AUDIO FILE EXISTS START
    audio_file_location = video_file_path[0 : video_file_path.rindex("\\") + 1]
    check_file = False
    for file_name in os.listdir(audio_file_location):
        if ".wav" in file_name:
            check_file = True
            break
        
    if check_file == False:
        sys.exit("Audio File not created.")
    else:
        return audio_file_path
    # else :
    #     audio_file_check = tkinter.Label(root, text = "Audio extracted from Video", font = ("Times New Roman", 12, "bold"))
    #     audio_file_check.pack()
        