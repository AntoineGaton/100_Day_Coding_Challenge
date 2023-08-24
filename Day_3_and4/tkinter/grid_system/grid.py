from tkinter import *

# Tk() is a function that creates a window
root = Tk()

# Creating a label widget
myLabel1 = Label(root, text="We are understanding the grid system!")
myLabel2 = Label(root, text="My name is Antoine Gaton!")

# The grid system allows us to place our widgets anywhere we want
# We can use the grid system to place our labels anywhere we want
myLabel1.grid(row=0, column=0) 
myLabel2.grid(row=1, column=5)  

root.mainloop()