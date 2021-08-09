import speech_recognition as sr
import moviepy.editor as mp
import os

clip = mp.VideoFileClip(r"task_video_1.mp4") 
 
clip.audio.write_audiofile(r"extracted_audio.wav")

# Extracting audio using ffmpeg library

command2wav = "ffmpeg -i task_video_1.mp4 -ab 256k -ar 44100 -vn extracted_audio.wav"

os.system(command2wav)

r = sr.Recognizer();

audio = sr.AudioFile("extracted_audio.wav")

with audio as source:
  audio_file = r.record(source)
  
# try:
#     print("Sphinx thinks you said " + r.recognize_sphinx(audio))
# except sr.UnknownValueError:
#     print("Sphinx could not understand audio")
# except sr.RequestError as e:
#     print("Sphinx error; {0}".format(e))


result = r.recognize_sphinx(audio_file)

with open("transcripted_text.txt",mode ='w') as file: 
   file.write("\n") 
   file.write(result) 
   file.write("\n")
  
print("Files are ready! check it out.")
   
   
   
