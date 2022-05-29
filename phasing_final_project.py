from email.mime import audio
import tkinter, os, sys
from PIL import Image

def line_break():
    line_space = tkinter.Label(root, text = "")
    line_space.pack()
    

video_file_path = ""
audio_file_path = ""
srt_file_path = ""

root = tkinter.Tk()

width = root.winfo_screenwidth()
space = (" " * (int(width)//8) + "         ")

root.title(space + "SRFP PROJECT BY KSHITIJ DWIVEDI")
 
root.iconbitmap("D:\Internship_SRFP\SRFP_2021\Learning GUI\icon.ico")

headline = tkinter.Label(root, text = "\nSUBTITLE (SRT FILE) GENERATOR AND ALIGNER", font = ("Times New Roman", 20, "bold"))

headline.pack()

line_break()

# GIF -- START
gif_label = tkinter.Label(root, text = "HOW IT WORKS", font = ("Times New Roman", 12, "bold"))
gif_label.pack()

gif_file = "D:\Internship_SRFP\SRFP_2021\Learning GUI\workflow_gui.gif"
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

line_break()

def button_method():
    
    # EXTRACTING AUDIO FROM VIDEO -- START
    global video_file_path, audio_file_path, srt_file_path
    
    video_file_path = file_path_data.get()
    
    if not os.path.isfile(video_file_path):
        sys.exit("ERROR! INCORRECT VIDEO FILE PATH")
        
    audio_file_path = video_file_path[:len(video_file_path)-4:] + "_extracted_audio.wav"
    
    mp4_2_wav = "ffmpeg -i " + video_file_path + " -ac 1 -ab 16000 -ar 48000 -vn " + audio_file_path + ""  # 16000 = 16kbps bit rate, 48000 = 48 kHz sampling rate

    os.system(mp4_2_wav)
    # -- END

    # CHECK IF AUDIO FILE EXISTS START
    audio_file_location = video_file_path[0 : video_file_path.rindex("\\") + 1]
    check_file = False
    for file_name in os.listdir(audio_file_location):
        if ".wav" in file_name:
            check_file = True
            break
        
    if check_file == False:
        sys.exit("Audio File not created.")
    else :
        audio_file_check = tkinter.Label(root, text = "Audio extracted from Video", font = ("Times New Roman", 12, "bold"))
        audio_file_check.pack()
        
    # print(os.listdir(audio_file_location))
    # END
    
    
    
    

    
submit_button = tkinter.Button(root, text = "Click here to Generate Subtitles!", bg = "red", fg = "white", padx = 10, pady = 5, command = button_method, font = ("Times New Roman", 12, "bold"))

submit_button.pack()

exit_button = tkinter.Button(root, text = "Exit Program", padx = 10, pady = 5, command = root.quit, font = ("Times New Roman", 12))
exit_button.pack(side = tkinter.BOTTOM)

root.mainloop()



