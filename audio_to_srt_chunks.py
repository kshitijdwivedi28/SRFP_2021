import os, sys
from re import sub

from pydub import AudioSegment
from pydub.silence import split_on_silence

from speech_recognition import Recognizer, AudioFile, UnknownValueError, RequestError


def converting_time(curr_time):
    hour = int((curr_time/60)/60)
    curr_time -= hour*60
    hour = '0' + str(hour) 
    
    minute = int(curr_time/60)
    curr_time -= minute*60
    if minute < 10:
        minute = '0' + str(minute)
    else:
        minute = str(minute) 
           
    seconds = int(curr_time)
    millisec = str(round(curr_time - seconds, 3))
    if millisec == '0':
        millisec = '000'
    else:
        millisec = millisec[2:]  
    if seconds < 10:
        seconds = '0' + str(seconds) + ',' + millisec
    else:
        seconds = str(seconds) + ',' + millisec
    
    final_time = hour + ':' + minute + ':' + seconds
    
    return final_time


audio_file_path = input("ENTER THE AUDIO FILE PATH : ")
transcript_file_path = input("ENTER THE TRANSCRIPT FILE PATH : ")
srt_file_path = input("ENTER THE SRT FILE PATH : ")

if not os.path.isfile(audio_file_path):
    sys.exit("ERROR! INCORRECT AUDIO FILE PATH")
elif not os.path.isfile(transcript_file_path):
    sys.exit("ERROR! INCORRECT TRANSCRIPT FILE PATH")
elif not os.path.isfile(srt_file_path):
    sys.exit("ERROR! INCORRECT SRT FILE PATH")


recorder = Recognizer()


time_transcript = []
srt_transcript = []
curr_time = 0
complete_transcript = ""
subtitles = ""

audio_file = AudioSegment.from_wav(audio_file_path)  
chunks = split_on_silence(audio_file,
    min_silence_len = 800,
    silence_thresh = audio_file.dBFS-14, 
    keep_silence = 50)

counter = 0

for i, audio_chunk in enumerate(chunks, start = 1):
    
    audio_file_chunk = os.path.join(f"chunk{i}.wav")
    
    audio_chunk.export(audio_file_chunk, format = "wav")
    
    duration = audio_chunk.duration_seconds
    
    time_transcript.append([i, round(curr_time, 3), round(curr_time + duration, 3)])
    
    curr_time += duration
    
    with AudioFile(audio_file_chunk) as source:
        counter += 1
        audio_record = recorder.record(source)
        
        try:
            transcript = recorder.recognize_google(audio_record)
        except (UnknownValueError, RequestError):
            print("ERROR! GOOGLE COULD NOT RECOGNIZE DATA.")
            print(f"THIS ERROR IS ENCOUNTERED AT AUDIO CHUNK {i}")
            srt_transcript.append("")
        else:
            transcript = f"{transcript.capitalize()}."
            complete_transcript += transcript + "\n"
            srt_transcript.append(transcript)
            
    os.remove(audio_file_chunk)

          

for i, time_value in enumerate(time_transcript):
    srt_block = str(time_value[0]) + "\n"
    
    start_time = converting_time(time_value[1])
    end_time = converting_time(time_value[2])
    
    srt_block += start_time + " --> " + end_time + "\n" + srt_transcript[i] + "\n\n"
    
    subtitles += srt_block


print(time_transcript)
print(srt_transcript)
print(subtitles)

srt_file_handler = open(srt_file_path, 'w')
srt_file_handler.write(subtitles)
srt_file_handler.close()

transcript_file_handler = open(transcript_file_path, 'w')
transcript_file_handler.write(complete_transcript)
transcript_file_handler.close()

print("\n\nPROGRAM COMPLETED SUCCESSFULLY. CHECK THE FILES! \n\n")
