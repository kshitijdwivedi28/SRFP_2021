import speech_recognition as sr
import moviepy.editor as mp

clip = mp.VideoFileClip(r"task_video_3.mp4") 
 
clip.audio.write_audiofile(r"task2_converted.wav")

r = sr.Recognizer();

audio = sr.AudioFile("task2_converted.wav")

with audio as source:
  audio_file = r.record(source)
  
result = r.recognize_google(audio_file)

with open("recognized.txt",mode ='w') as file: 
   file.write("\n") 
   file.write(result) 
   print("Ready!")
   