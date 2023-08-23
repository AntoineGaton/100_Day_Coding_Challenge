#import tkinter
from tkinter import *

# NOTE: Everything in tkinter is a widget!

# Create the main window
root = Tk()

# NOTE: There's a two step process to adding a widget to the window. 
# Step #1: Create a label widget
message = Label(text="Hello World!")

# Step #2: Add the label widget to the window
message.pack()

# This is the main loop that will keep the window open
root.mainloop()