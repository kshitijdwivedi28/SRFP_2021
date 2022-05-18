# importing module
import tkinter

# creating object 
root = tkinter.Tk()

# Creating Label Widget which puts up a text on screen
headline = tkinter.Label(root, text = "SRFP PROJECT - SUBTITLE (SRT FILE) GENERATOR")

# Putting it up on screen and pack the window size as much as the text within, puts the text in center of the window
headline.pack()

# Alternative of pack is grid(), here the positioning is relative. So, if no data in cells 0-4 
# looks like position of row 5, is like the position of row 0 and same is with columns
# myLabel.grid(row = 5, column = 5) 
# For now using pack only.


# Inputting file path from user and printing it
file_path = tkinter.Label(root, text = "Enter video file path : ")
file_path.pack(side = tkinter.LEFT)
enter_data = tkinter.Entry(root, width = 50)
enter_data.pack(side = tkinter.LEFT)



# Note, wanted to use grid here for printing the data but can't because we can only use either pack or grid.

# method to execute when button is clicked
def button_method():
    # test
    # new_text = tkinter.Label(root, text = "Button is clicked.")
    # new_text.pack(side = tkinter.BOTTOM)
    
    # get() in used to take the input data from the input entry field
    entered_file_path = tkinter.Label(root, text = "Entered video file path is : " + enter_data.get())
    entered_file_path.pack(side = tkinter.BOTTOM)
    
    # Todo - when button clicked run the python script to generate srt - 
    # So will provide options through 5 buttons first
    # Input files accordingly
    # Generate the output 
     
    # 1. Extract Audio
    # 2. Audio to Transcript
    # 3. Audio to Subtitles (By Splitting on Silence)
    # 4. Audio to Subtitles (By Dividing the text into constant time frames)
    # 5. Transcript to Subtitles (Forced Alignment)
    
    
# Creating buttons
# Increase the size of the button using padx / pady
# Disable the button with state = disable
# Can change text color and backgroud color in button using fg = "blue" for font, and bg = "red" also background, it also accepts hexcode of colors
# To make buttons to do some work when clicked, define a function and call it using command = while creating button
submit_button = tkinter.Button(root, text = "Click here to Generate Subtitles!", bg = "red", fg = "white", padx = 10, pady = 5, command = button_method, font = ("Times New Roman", 10, "bold"))

# Put up the button on screen
# Using pack only for keeping the button in center
submit_button.pack()

# Hovering on the screen and keeping the program running until the window is closed
root.mainloop()
