import wave, math, contextlib, os, sys
import speech_recognition as sr
import datetime

audio_file_path = input("ENTER THE AUDIO FILE PATH : ")
transcript_file_path = input("ENTER THE TRANSCRIPT FILE PATH : ")
srt_file_path = input("ENTER THE SRT FILE PATH : ")

if not os.path.isfile(audio_file_path):
    sys.exit("ERROR! INCORRECT AUDIO FILE PATH")
elif not os.path.isfile(transcript_file_path):
    sys.exit("ERROR! INCORRECT TRANSCRIPT FILE PATH")
elif not os.path.isfile(srt_file_path):
    sys.exit("ERROR! INCORRECT SRT FILE PATH")

with contextlib.closing(wave.open(audio_file_path, 'r')) as audio_file:
    frames = audio_file.getnframes() 
    rate = audio_file.getframerate()  
    duration = frames / float(rate)  

total_segments = math.ceil(duration / 5)

print("\n AUDIO LENGTH CALCULATED ")  


print("\nNo. of Audio Frames = ", frames)
print("\nAudio Frame Rate = ", rate)
print("\nDuration of Audio File = ", duration)


iterator_audio_segment = 0
start_time = datetime.datetime(2021, 8, 20, 0, 0, 0)
current_time = start_time 
end_time = 0  
audio_segment_duration = 5


print("\nSTART TIME = ", start_time)
print("\nCURRENT TIME = ", current_time)
print("\nSRT Variables initialized successfully")


recog = sr.Recognizer()

srt_file_handler = open(srt_file_path, 'w+')


transcript_file_handler = open(transcript_file_path, 'w+')


for audio_segment in range(total_segments):
    with sr.AudioFile(audio_file_path) as source:
  
        record_audio = recog.record(source, offset = audio_segment * audio_segment_duration, duration = audio_segment_duration)

        text = recog.recognize_google(record_audio)#, language = 'en-IN')

        transcript_file_handler.write(text)
        # print(text)
        
        if audio_segment == 0:
            current_time = start_time  
        else:
            current_time = end_time  


        end_time = current_time + datetime.timedelta(0, audio_segment_duration)  
        str_current_time = str(current_time.time())
        str_end_time = str(end_time.time())

        srt_file_handler.write(str(audio_segment + 1))  
        srt_file_handler.write("\n")  
        srt_file_handler.write(str_current_time) 
        srt_file_handler.write(" --> ")  
        srt_file_handler.write(str_end_time)  
        srt_file_handler.write("\n")  
        srt_file_handler.writelines(text)  
        srt_file_handler.write("\n\n") 

print("PROGRAM COMPLETED SUCCESSFULLY")
srt_file_handler.close()
transcript_file_handler.close()


# my 1st method