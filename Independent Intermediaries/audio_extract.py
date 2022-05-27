import os, sys

# user input file path --dynamic

# Audio Extraction through ffmpeg library

video_file_path = input("ENTER VIDEO FILE PATH : ")

if not os.path.isfile(video_file_path):
    sys.exit("ERROR! INCORRECT VIDEO FILE PATH")

audio_file_path = video_file_path[:len(video_file_path)-4:] + "_extracted_audio.wav"

# customized input just for seperate running will not be integrated with the gui
sampling_rate = int(input("ENTER SAMPLING RATE FOR AUDIO OUTPUT (DEFAULT 44100) (in Hz) : "))
bit_rate = int(input("ENTER BIT RATE FOR AUDIO OUTPUT (DEFAULT - 16000) (in bps) : "))

mp4_2_wav = "ffmpeg -i " + video_file_path + " -ac 1 -ab " + str(bit_rate) + " -ar " + str(sampling_rate) + " -vn " + audio_file_path + ""

os.system(mp4_2_wav)

print("\n\nAUDIO EXTRACTED SUCCESSFULLY USING FFMPEG \n\n")


# Audio Extraction through moviepy

# import moviepy.editor as mp

# video_file_path = input("ENTER VIDEO FILE PATH : ")
# audio_file_path = input("ENTER AUDIO FILE PATH : ")

# audio_clip = mp.VideoFileClip(video_file_path) 
 
# audio_clip.audio.write_audiofile(audio_file_path)

# print("\n\nAUDIO EXTRACTED SUCCESSFULLY USING MOVIEPY \n\n")


# Advantages of FFMPEG as it gives us more control on the characterstics of the output audio file such as 
# sampling rate, bit rate etc. and can handle all the types audio wav, flac, etc




# -vn - Indicates that we have disabled video recording in the output file.
# -ar - Set the audio frequency of the output file. The common values used are  22050, 44100, 48000 Hz.
# -ac - Set the number of audio channels.
# -ab - Indicates the audio bitrate.
# -f - Output file format. In our case, it's mp3 format.

# ffmpeg  - details https://ostechnix.com/20-ffmpeg-commands-beginners/