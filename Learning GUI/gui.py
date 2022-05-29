# importing module
import tkinter
from PIL import Image

# creating object 
root = tkinter.Tk()

# No feature in tkinter for adjusting title, so calculating the space for positioning the title customized
width = root.winfo_screenwidth()
space = (" " * (int(width)//15))

# Title of the Window
root.title(space + "SRFP PROJECT BY KSHITIJ DWIVEDI")
 
# icon at the top left side
root.iconbitmap("D:\Internship_SRFP\SRFP_2021\Learning GUI\icon.ico")

# Creating Label Widget which puts up a text on screen
headline = tkinter.Label(root, text = "\nSUBTITLE (SRT FILE) GENERATOR AND ALIGNER", font = ("Times New Roman", 20, "bold"))

# Putting it up on screen and pack the window size as much as the text within, puts the text in center of the window
headline.pack()

# Alternative of pack is grid(), here the positioning is relative. So, if no data in cells 0-4 
# looks like position of row 5, is like the position of row 0 and same is with columns
# myLabel.grid(row = 5, column = 5) 
# For now using pack only.

# As there's no widget for putting space in back. So,customized for creating the space between widgets
line_space = tkinter.Label(root, text = "")
line_space.pack()


# Built and inserting a self created gif 
# GIF -- START
gif_label = tkinter.Label(root, text = "HOW IT WORKS", font = ("Times New Roman", 12, "bold"))
gif_label.pack()


gif_file = "D:\Internship_SRFP\SRFP_2021\Learning GUI\gif_for_gui.gif"
file_info = Image.open(gif_file)

# getting the number of frames from gif, as tkinter can render one frame at a time, so will loop through frames
# present the gif
frames = file_info.n_frames

# creating list of PhotoImage objects for each frames
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


# Inputting file path from user and printing it
file_path_label = tkinter.Label(root, text = "\nEnter Video File Path", font = ("Times New Roman", 12))
file_path_label.pack()

file_path_data = tkinter.Entry(root, width = 50)
file_path_data.pack()
# For default input in the 0th Input field
file_path_data.insert(0, "Enter Video file path :")

line_space = tkinter.Label(root, text = "")
line_space.pack()



# Note, wanted to use grid here for printing the data but can't because we can only use either pack or grid.

# method to execute when button is clicked
def button_method():
    # test
    # new_text = tkinter.Label(root, text = "Button is clicked.")
    # new_text.pack(side = tkinter.BOTTOM)
    
    # get() in used to take the input data from the input entry field
    entered_file_path = tkinter.Label(root, text = "Entered video file path is : " + file_path_data.get())
    entered_file_path.pack()
    
    
    
    
# Creating buttons
# Increase the size of the button using padx / pady
# Disable the button with state = disable
# Can change text color and backgroud color in button using fg = "blue" for font, and bg = "red" also background, it also accepts hexcode of colors
# To make buttons to do some work when clicked, define a function and call it using command = while creating button
submit_button = tkinter.Button(root, text = "Click here to Generate Subtitles!", bg = "red", fg = "white", padx = 10, pady = 5, command = button_method, font = ("Times New Roman", 12, "bold"))

# Put up the button on screen
# Using pack only for keeping the button in center
submit_button.pack()

# exit button
exit_button = tkinter.Button(root, text = "Exit Program", padx = 10, pady = 5, command = root.quit, font = ("Times New Roman", 12))
exit_button.pack(side = tkinter.BOTTOM)

# Hovering on the screen and keeping the program running until the window is closed
root.mainloop()




