import speech_recognition as sr
import moviepy.editor as mp

clip = mp.VideoFileClip(r"task_video_1.mp4") 
 
clip.audio.write_audiofile(r"task2_converted.wav")

r = sr.Recognizer();

audio = sr.AudioFile("task2_converted.wav")

with audio as source:
  audio_file = r.record(source)
  
# try:
#     print("Sphinx thinks you said " + r.recognize_sphinx(audio))
# except sr.UnknownValueError:
#     print("Sphinx could not understand audio")
# except sr.RequestError as e:
#     print("Sphinx error; {0}".format(e))


result = r.recognize_sphinx(audio_file)

with open("recognized.txt",mode ='w') as file: 
   file.write("\n") 
   file.write(result) 
   print("Ready!")
   
   
   
