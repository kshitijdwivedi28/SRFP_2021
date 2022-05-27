import speech_recognition as sr_module, os, sys

# user input paths 

audio_file_path = input("ENTER AUDIO FILE PATH : ")
transcript_file_path = input("ENTER TRANSCRIPT FILE PATH :")

if not os.path.isfile(audio_file_path):
    sys.exit("ERROR! INCORRECT AUDIO FILE PATH")
elif not os.path.isfile(transcript_file_path):
    sys.exit("ERROR! INCORRECT TRANSCRIPT FILE PATH")


recorder = sr_module.Recognizer()

audio_file = sr_module.AudioFile(audio_file_path)

with audio_file as source:
    # modification 1 - adjust for ambient noise 
    recorder.adjust_for_ambient_noise(source, duration=2)
    record_data = recorder.record(source)


try:
    print("TRANSCRIPTING DATA : ")
    # modification 2 - adding language. Hardly any difference between the detected language and provided language
    result_data = recorder.recognize_google(record_data, language='en-IN')
except recorder.UnknownValueError:
    print("GOOGLE COULD NOT RECOGNIZE DATA. ERROR!")
except recorder.RequestError:
    print("CANNOT REQUEST TO GOOGLE SPEECH TO TEXT API. INTERNET NOT CONNECTED OR GOOGLE SERVER IS DOWN.")

# print(result_data)

with open(transcript_file_path, mode ='w+') as transcript_file_handler: 
   transcript_file_handler.write(result_data) 
   transcript_file_handler.write("\n")
  
print("\n\nPROGRAM COMPLETED SUCCESSFULLY. CHECK THE FILES! \n\n")