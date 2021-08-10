import wave, math, contextlib
import speech_recognition as sr
import moviepy.editor as mp

import datetime

transcribed_audio_file_name = "output/task_audio.wav"
video_file_name = "task_video.mp4"

# Moviepy library being used for audio extraction 

# audioclip = AudioFileClip(video_file_name)
audioclip = mp.VideoFileClip(video_file_name)
audioclip.audio.write_audiofile(transcribed_audio_file_name)


#FFmpeg library used for audio extraction

command2wav = "ffmpeg -i task_video_1.mp4 -ab 256k -ar 44100 -vn extracted_audio.wav"

os.system(command2wav)

# for finding the total length of the audio file
with contextlib.closing(wave.open(transcribed_audio_file_name,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    
total_segments = math.ceil(duration/10)

r = sr.Recognizer()
i = 0
start_time = datetime.datetime(2021,7,30,0,0,0)
current_time = start_time
end_time = 0
time_add = 10

#building SRT file
#another file is also being made for simple transcripted text

f1 = open("output/transcription_using_wave.txt", 'w')
f2 = open("output/srt_file.srt",'w')

for i in range(0, total_segments):
    with sr.AudioFile(transcribed_audio_file_name) as source:
        audio = r.record(source, offset=i*10, duration=10)                #subclip function can also be used to divide the audio into segments
    
    text = r.recognize_google(audio)
    
    f1.write(text)
    f1.write("\n\n")

    if i == 0:
        current_time = start_time
        end_time = current_time + datetime.timedelta(0,time_add)

    if i > 0:
        current_time = end_time
        end_time = current_time + datetime.timedelta(0,time_add)
    
    str_current_time = str(current_time.time())
    str_end_time = str(end_time.time())
    
    f2.write(str(i+1))
    f2.write("\n")
    f2.write(str_current_time)
    f2.write(" --> ")
    f2.write(str_end_time)
    f2.write("\n")
    f2.write(text)
    f2.write("\n\n")
    
f1.close()
f2.close()

print("\n\nHey, It's done. Check your files in the output folder.")


