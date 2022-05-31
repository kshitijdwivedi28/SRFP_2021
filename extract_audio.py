# os, sys for executing system commands in command line
import os, sys 

def video_to_audio(video_file_path):
    
    # IF THE INPUT VIDEO FILE PATH IS VALID
    if not os.path.isfile(video_file_path):
        sys.exit("ERROR! INCORRECT VIDEO FILE PATH")
        
    audio_file_path = video_file_path[:len(video_file_path)-4:] + "_extracted_audio.wav"
    
    # IF AUDIO FILE ALREADY EXISTS
    if (os.path.isfile(audio_file_path)):
        return audio_file_path
    
    # EXTRACTING AUDIO
    # -i selects the input file
    # -q:a 0 outputs audio with variable bitrate and the highest quality. 
    # -map 0:a selects all audio streams
    # -ab defines the audio bit rate (in bps)
    # -ar defines the audio frame rate (in Hz)
    # -vn removes the video, and only selects the audio
    mp4_2_wav = "ffmpeg -i " + video_file_path + " -map 0:a -ab 8000 -ar 16000 -q:a 0 -vn " + audio_file_path + "" 

    os.system(mp4_2_wav)

    # IF AUDIO FILE HAS BEEN CREATED
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
        