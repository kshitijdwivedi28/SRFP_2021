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


print("\n AUDIO EXTRACTED SUCCESSFULLY ")           # check point message


# For finding the total length of the audio file
# The wave library is used to open the audio file to calculate the number of frames and the framerate with which duration of file has been calculated
# contextlib.closing  works with the with statement to inform the context manager when the code block is entered and exited
with contextlib.closing(wave.open(audio_file_path,'r')) as audio_file:
    frames = audio_file.getnframes()                                          # Total number of audio frames is stored in frames variable     
    rate = audio_file.getframerate()                                          # Sampling Frequency of the audio file is stored in rate variable
    duration = frames / float(rate)                                           # Duration is calculated using frames and rate variable
    
# Segmenting audio into parts of 60 secs to be transcribed into text and thereby calculating total segments of the audio
total_segments = math.ceil(duration/60)  

   
print("\n AUDIO LENGTH CALCULATED ")                  # checkpoint message

# flag messages to check and verify the content
print("\nNo. of Audio Frames = ",frames)             
print("\nAudio Frame Rate = ",rate)
print("\nDuration of Audio File = ",duration)


# Building up the SRT file 
iterator_audio_segment = 0
start_time = datetime.datetime(2021,8,20,0,0,0)     # time to instatiate the starting time for srt file       
current_time = start_time                           # For the first segment the start time = current time 
end_time = 0                                        # end time for the audio file, will be subsequently increase as audio segments are parsed
audio_segment_duration = 60                                       # time for each audio segment 

# flag messages to check and verify the content
print("\nSTART TIME = ",start_time)
print("\nCURRENT TIME = ",current_time)
print("\nSRT Variables initialized successfully")

# Initliazing object of Recognizer class
recog = sr.Recognizer()

# Subtitle/Captions file in SRT format
srt_file = open(r"output/subtitles.srt",'w')

# Transcript File in txt format
transcript_file = open(r"output/transcription.txt", 'w')

# loop to transcribe each segment of audio into text 
for audio_segment in range(total_segments):
    with sr.AudioFile(audio_file_path) as input:              
        
        # audio input for a particular point of time 
        # offset flag shifts the time from current time 
        # duration flag marks the total time of the audio input
        record_audio = recog.record(input, offset = audio_segment*audio_segment_duration, duration = audio_segment_duration)       
        
        # transcribing audio into text using Google Web Speech to Text API [free of cost, limited to 50 transcriptions per day]
        text = recog.recognize_google(record_audio, language = 'en-IN')
       
        # Adding transcripted text to the transcript file
        transcript_file.write("Transcript of the Video : ")
        transcript_file.write(text)
        transcript_file.write("\n\n")
        
        # Setting up current_time for the audio segments 
        if audio_segment == 0:
            current_time = start_time                                              # For the first audio_segment current time of audio = starting time of audio
        else :
            current_time = end_time                                                # For the other audio_segments current_time = end_time of the previous audio segment
           
         end_time = current_time + datetime.timedelta(0,audio_segment_duration)    # End Time being assigned for the audio_segment by adding up the audio_segment_duration to the current_time of audio_segment
           
        # Time values being changed to string to be written to the SRT File 
        str_current_time = str(current_time.time())
        str_end_time = str(end_time.time())
        
        
        # Writing data into the subscript file considering the format of (.srt) file
        srt_file.write(str(audio_segment+1))                                      # Audio Segment Number as a header for the subscript
        srt_file.write("\n")                                                      # Newline character for writing data into next line 
        srt_file.write(str_current_time)                                          # Starting time for the subscript
        srt_file.write("\n")                                                      # Newline character for writing data into next line
        srt_file.write(" --> ")                                                   # For aligning the data according to (.srt) format
        srt_file.write(str_end_time)                                              # Ending time for the subscript
        srt_file.write("\n")                                                      # Newline character for writing data into next line
        srt_file.write(text)                                                      # Writing transcription into the file
        srt_file.write("\n\n")                                                    # Newline character for writing data into next line (also leaving a line empty considering the (.srt) format
 
# Closing files 
srt_file.close()
transcript_file.close()
 
        
    
