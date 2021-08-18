# Importing Dependencies 

# Used for handling audio file in .wav format and open in up as wave read_object to calculate length of file 
import wave

# Used for ceil() for the upper bound of the length of the audio file while segmenting it in to parts
import math

# Used for contextlib.closing as it works with the with statement to inform the context manager when the code block is entered and exited. 
import contextlib          

# Used for converting the audio into text 

import speech_recognition as sr

# Used for directing and calculating timestamps for building up on SRT file
import datetime

# Used for extracting audio from the video file
import moviepy.editor as mp

# Used for executing commands using os.system() method
import os




# Video File path
video_file_path = r"input/task_video.mp4"

# Audio file path
audio_file_path = r"output/task_audio.wav"






# Extracting audio from video using FFmpeg library
# -i switch is used specify the path/filename of the input video
# -ab switch is used to save the audio as a 256kbps WAV audio file.
# -ar switch is used for the frequency/frame rate of the audio.
# -vn switch extracts the audio portion from a video.

command_mp42wav = "ffmpeg -i "+video_file_path+" -ab 256k -ar 44100 -vn "+audio_file_path+""

# os.system() method is used to execute the ffmpeg library in command line
os.system(command_mp42wav)





# For finding the total length of the audio file
# The wave library is used to open the audio file to calculate the number of frames and the framerate with which duration of file has been calculated
# contextlib.closing  works with the with statement to inform the context manager when the code block is entered and exited
with contextlib.closing(wave.open(audio_file_path,'r')) as audio_file:
    frames = audio_file.getnframes()                                          # Total number of audio frames is stored in frames variable     
    rate = audio_file.getframerate()                                          # Sampling Frequency of the audio file is stored in rate variable
    duration = frames / float(rate)                                           # Duration is calculated using frames and rate variable
    
               
    

