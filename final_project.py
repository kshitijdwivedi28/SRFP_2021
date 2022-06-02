import tkinter, os, sys
from PIL import Image
import srt_with_transcript, srt_without_transcript, extract_audio

def subtitle_sync(video_file_path, srt_file_path):
    
    new_srt_file_path = srt_file_path[:len(srt_file_path)-4:] + "_optimized.srt"
    command = f"ffsubsync {video_file_path} -i {srt_file_path} -o {new_srt_file_path}"    
    os.system(command)
    
    if (os.path.isfile(new_srt_file_path)):
        os.remove(srt_file_path) # can be commented to look for differences by using ffsubsync and without using it
        return new_srt_file_path    
    else:
        return ""
    

def submit_button_action():
    video_file_path = file_path_data.get()
    audio_file_path = extract_audio.video_to_audio(video_file_path)
    
    if (with_transcript_option):
        transcript_file_path = transcript_file_path_data.get()
        
        if len(transcript_file_path) > 0 and not os.path.isfile(transcript_file_path):
            sys.exit("ERROR! INCORRECT TRANSCRIPT FILE PATH")
        
        srt_file_path = video_file_path[ : len(video_file_path)-4 : ] + "_subtitles.srt"
        
        # res = srt_with_transcript.align_audio_with_transcript(audio_file_path = audio_file_path, transcript_file_path = transcript_file_path, srt_file_path = srt_file_path)
        srt_without_transcript.audio_to_srt_chunks(audio_file_path, srt_file_path)
        new_srt_file_path = srt_with_transcript.force_align(transcript_file_path, srt_file_path)
        final_srt_file_path = subtitle_sync(video_file_path, new_srt_file_path)
        
        if (os.path.isfile(final_srt_file_path)):
            os.remove(srt_file_path)
            res_label = tkinter.Label(root, text = f"\nSubtitles have been generated successfully. You can find them at location : {srt_file_path}", font = ("Times New Roman", 12, "bold"), fg = "green")
            res_label.pack()
        else:
            sys.exit("SYSTEM ERROR! REFER DEVELOPER TO RESOlVE")
         
    else:
        srt_file_path = video_file_path[ : len(video_file_path)-4 : ] + "_subtitles_without_transcript.srt"
        srt_without_transcript.audio_to_srt_chunks(audio_file_path, srt_file_path)
        srt_file_path = subtitle_sync(video_file_path, srt_file_path)
        if (os.path.isfile(srt_file_path)):
            res_label = tkinter.Label(root, text = f"\nSubtitles have been generated successfully. You can find them at location : {srt_file_path}", font = ("Times New Roman", 12, "bold"), fg = "green")
            res_label.pack()
        else:
            sys.exit("SYSTEM ERROR! REFER DEVELOPER TO RESOlVE")
            

    
    
def with_transcript_action():
    global with_transcript_option
    with_transcript_option = True
    
    transcript_file_path_label = tkinter.Label(root, text = "\nEnter Transcript File Path", font = ("Times New Roman", 12, "bold"))
    transcript_file_path_label.pack()

    transcript_file_path_data.pack()


def without_transcript_action():
    continue_ahead_label = tkinter.Label(root, text = "\nYou are all set. Click on the Red Button below to generate Subtitles file.", font = ("Times New Roman", 12, "bold"))
    continue_ahead_label.pack()
    
    
def line_break():
    line_space = tkinter.Label(root, text = "")
    line_space.pack()
    
 
video_file_path = ""
audio_file_path = ""
transcript_file_path = ""
srt_file_path = ""
with_transcript_option = False

root = tkinter.Tk()

width = root.winfo_screenwidth()
space = (" " * (int(width)//8) + "         ")

root.title(space + "SRFP PROJECT BY KSHITIJ DWIVEDI")
 
root.iconbitmap("./Learning GUI/icon.ico")

headline = tkinter.Label(root, text = "\nSUBTITLE (SRT FILE) GENERATOR AND ALIGNER", font = ("Times New Roman", 20, "bold"))

headline.pack()

line_break()

# GIF -- START
gif_label = tkinter.Label(root, text = "HOW IT WORKS", font = ("Times New Roman", 16, "bold"))
gif_label.pack()

gif_file = "./Learning GUI/workflow_gui.gif"
file_info = Image.open(gif_file)

frames = file_info.n_frames

gif_frames = [tkinter.PhotoImage(file = gif_file, format = f"gif -index {i}") for i in range(frames)]

gif_label = tkinter.Label(root, image="")
gif_label.pack()

count = 0
anim = None

def animation(count):
    global anim
    single_frame = gif_frames[count]

    gif_label.configure(image = single_frame)
    count += 1
    
    if count == frames:
        count = 0
        
    anim = root.after(2000, lambda :animation(count))

animation(count)
# GIF -- END

file_path_label = tkinter.Label(root, text = "\nEnter Video File Path", font = ("Times New Roman", 12, "bold"))
file_path_label.pack()

file_path_data = tkinter.Entry(root, width = 100)
file_path_data.pack()

transcript_file_path_data = tkinter.Entry(root, width = 100)

line_break()

# adding buttons for options using 
button_frame = tkinter.Frame(root)
button_frame.pack()

with_transcript_button = tkinter.Button(button_frame, text = "Generate Subtitles using Transcript", font = ("Times New Roman", 12), padx = 5, pady = 5, command = with_transcript_action)
with_transcript_button.grid(row = 0, column = 0, padx = 5, pady = 5)

without_transcript_button = tkinter.Button(button_frame, text = "Generate Subtitles without using Transcript", font = ("Times New Roman", 12), padx = 5, pady = 5, command = without_transcript_action)
without_transcript_button.grid(row = 0, column = 1, padx = 5, pady = 5)

exit_button = tkinter.Button(root, text = "Exit Program", padx = 10, pady = 5, command = root.quit, font = ("Times New Roman", 12, "bold"))
exit_button.pack(side = tkinter.BOTTOM)

submit_button = tkinter.Button(root, text = "Click here to Generate Subtitles!", bg = "red", fg = "white", padx = 10, pady = 5, command = submit_button_action, font = ("Times New Roman", 12, "bold"))
submit_button.pack(side = tkinter.BOTTOM)

root.mainloop()


# ---- PROGRAM ENDS HERE ----