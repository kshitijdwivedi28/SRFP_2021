import wave, contextlib, datetime, os, sys

def extracting_time(curr_time):
    
    hour = int((curr_time/60)/60)
    curr_time -= hour*60
    
    minute = int(curr_time/60)
    curr_time -= minute*60
           
    seconds = int(curr_time)
    
    return hour, minute, seconds


def get_word_count(transcript_file_path):
    
    word_count = 0
    
    with open(transcript_file_path, 'r') as transcript_file_handler:
        file_data = transcript_file_handler.read()

    for ch in file_data:
        if (ch in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
            word_count += 1
            
    return word_count/4.7


def count_words(data):
    word_count = 0
    for ch in data:
        if (ch in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
            word_count += 1

    return word_count/4.7
        

audio_file_path = input("ENTER AUDIO FILE PATH : ")
transcript_file_path = input("ENTER TRANSCRIPT FILE PATH : ")
srt_file_path = input("ENTER SRT FILE PATH : ")

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

hours, minutes, seconds = extracting_time(duration)

# print(duration, hours, minutes, seconds)

transcript_file_handler = open(transcript_file_path, 'r')
transcript_data_lines = transcript_file_handler.readlines()
transcript_file_handler.close()

total_words = get_word_count(transcript_file_path)

word_time = duration/total_words

start_time = datetime.datetime(2022, 2, 28, 0, 0, 2)
current_time = start_time
max_time = datetime.datetime(2022, 2, 28, hour = hours, minute = minutes, second = seconds)

for i, line in enumerate(transcript_data_lines):
    if line == '\n':
        continue
    else:
        srt_block = i+1
        data = line
        
        time_add = len(data.split())*word_time
        end_time = current_time + datetime.timedelta(0, time_add)
        str_current_time = str(current_time.time())
        str_end_time = str(end_time.time())
        
        if '.' in str_current_time:
            index = str_current_time.find('.')
            str_current_time = str_current_time[0:index] + ',' + str_current_time[index+1:index+4]
        
        if '.' in str_end_time:
            index = str_end_time.find('.')
            str_end_time = str_end_time[0:index] + ',' + str_end_time[index+1:index+4]

        with open(srt_file_path, 'a') as srt_file_handler:
            srt_file_handler.write(str(srt_block))
            srt_file_handler.write("\n")
            srt_file_handler.write(str_current_time)
            srt_file_handler.write(" --> ")
            srt_file_handler.write(str_end_time)
            srt_file_handler.write("\n")
            srt_file_handler.write(data)
            srt_file_handler.write("\n")    
            
        current_time = end_time
    
    
print("\n\nPROGRAM COMPLETED SUCCESSFULLY. CHECK THE FILES! \n\n")
