from tkinter import *

root = Tk()

# Creating a function that will be executed when the button is clicked
def myClick():
    # Creating a label widget
    myLabel = Label(root, text="Look! I clicked a Button!!")
    # Packing the label widget
    myLabel.pack()

button1 = Button(root, text="Button #1", command=myClick, fg="blue", bg="red")
button2 = Button(root, text="Button #2", command=myClick, fg="green", bg="yellow")
button3 = Button(root, text="Button #3",  command=myClick, fg="purple", bg="orange")

button1.pack()
button2.pack()
button3.pack()

root.mainloop()