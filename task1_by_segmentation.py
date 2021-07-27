import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

command2wav = "ffmpeg -i task_video_3.mp4 -ab 256k -ar 11025 -vn audio_google_video_3.wav"

os.system(command2wav)

print("\nExtracted Audio from Video Successfully.\n")

path = "audio_google_video_3.wav"
audio = AudioSegment.from_wav(path)
f = open("transcript.txt", "w+")
chunks = split_on_silence(audio) #, min_silence_len = 500, silence_thresh = -16) #value in ms
os.mkdir('audio_chunks')
os.chdir('audio_chunks')
i = 0
for chunk in chunks:
    chunk_silent = AudioSegment.silent(duration = 10) #value in ms
    audio_chunk = chunk_silent + chunk + chunk_silent
    print("saving chunk{0}.wav".format(i))
    audio_chunk.export("./chunk{0}.wav".format(i), bitrate ='192k', format ="wav")
    filename = 'chunk'+str(i)+'.wav'
    print("Processing chunk "+str(i))
    file = filename
    r = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio_listened = r.listen(source)
        rec = r.recognize_google(audio_listened)
        f.write(rec+". ")
        i += 1

os.chdir('..')
