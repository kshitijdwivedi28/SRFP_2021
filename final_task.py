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


# Extracting audio from video using FFmpeg library
# -i switch is used specify the path/filename of the input video
# -ab switch is used to save the audio as a 256kbps WAV audio file.
# -ar switch is used for the frequency/frame rate of the audio.
#	-vn switch extracts the audio portion from a video.

command_mp42wav = "ffmpeg -i task_video.mp4 -ab 256k -ar 44100 -vn task_audio.wav"

# os.system() method is used to execute the ffmpeg library in command line
os.system(command_mp42wav)


