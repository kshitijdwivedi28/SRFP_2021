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
