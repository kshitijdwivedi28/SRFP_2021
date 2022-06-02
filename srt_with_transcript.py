import wave, contextlib, datetime, os
from fuzzywuzzy import fuzz

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
        sentences = file_data.split()
        
        for word in sentences:
            if word == '\n':
                continue
            else:
                word_count += 1
                
    return word_count


def align_audio_with_transcript(audio_file_path, transcript_file_path, srt_file_path):

    with contextlib.closing(wave.open(audio_file_path, 'r')) as audio_file:
        frames = audio_file.getnframes() 
        rate = audio_file.getframerate()  
        duration = frames / float(rate)

    hours, minutes, seconds = extracting_time(duration)

    transcript_file_handler = open(transcript_file_path, 'r')
    transcript_data_lines = transcript_file_handler.readlines()
    transcript_file_handler.close()

    total_words = get_word_count(transcript_file_path)

    word_time = duration/total_words

    start_time = datetime.datetime(2022, 5, 30, 0, 0, 2)
    current_time = start_time
    max_time = datetime.datetime(2022, 5, 30, hour = hours, minute = minutes, second = seconds)

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
    
    return True

    
def force_align(transcript_file_path, input_srt_file_path):
    
    print("INPUT SRT PATH - ", input_srt_file_path)
    
    output_srt_file_path = input_srt_file_path[:len(input_srt_file_path)-4:] + "_with_transcript.srt" 
    
    with open(input_srt_file_path, 'r') as read_srt:
        srt_lines = read_srt.readlines()

    with open(transcript_file_path, 'r') as tfile:
        transcript_data = tfile.read()
    
    transcript_words = transcript_data.split()
        
    final_captions = []
    initial_captions = []
    for caption in srt_lines:
        if caption[0] not in "0123456789" and caption[0] != "\n":
            
            initial_captions.append(caption)
            
            total_caption_words = len(caption.split())
            transcript = []
            for index in range(0, len(transcript_words), total_caption_words):
                curr = ' '.join(transcript_words[index : index + total_caption_words])
                transcript.append(curr)
            
            max_score = 0.0
            possible_caption = ""
            
            for sentence in transcript :
                # print(caption, sentence, fuzz.ratio(caption, sentence))
                if (fuzz.ratio(caption, sentence) >= max_score):
                    max_score = fuzz.ratio(caption, sentence)
                    possible_caption = sentence
                
            final_captions.append(possible_caption)
            transcript_words = transcript_words[total_caption_words::]
            
    index = 0
    with open(output_srt_file_path, 'w') as srtfile:
        for line in srt_lines:
            if line[0] not in "0123456789" and line[0] != "\n":
                srtfile.write(final_captions[index])
                srtfile.write("\n")
                index += 1
            else:
                srtfile.write(line)
                    
    if os.path.isfile(output_srt_file_path):
        return output_srt_file_path
    else:
        return ""
            