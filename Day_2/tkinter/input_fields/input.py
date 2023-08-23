from tkinter import *

root = Tk() 

# Creating an input field
e = Entry(root, width=50, borderwidth=5, fg="blue", bg="red")
e.insert(0, "Enter Your Name")
e.pack()

# Creating a function that will be executed when the button is clicked
def myClick():
    hello = "Hello " + e.get() + "!"
    # Getting the text from the input field
    myLabel = Label(root, text=hello)
    myLabel.pack()
    

# Creating a button
myButton = Button(root, text="Submit", command=myClick, fg="blue", bg="red")
myButton.pack()

root.mainloop()