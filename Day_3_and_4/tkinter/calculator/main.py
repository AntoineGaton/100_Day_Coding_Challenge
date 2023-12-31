"""
Things To Do:
- Fix bug with calculations.
- Refactor Design.
- Refactor Code.
- Add a decimal button.
- Add a delete button.
- Add a backspace button.
- Add a square root button.
- Add a power button.
- Add a percentage button.
- Add a negative/positive button.
- Add pi button.
"""

from tkinter import *

root = Tk()

# Setting the title of the window
root.title("Simple Calculator")
# Locking the size of the window
root.resizable(False, False)

# Creating an input field
e = Entry(root, width=50, borderwidth=5, font=("Arial", 10))
# Placing the input field on the screen
e.grid(row=0, column=0, columnspan=5, padx=30, pady=30)

def button_click(number):
    # Gets the current input field value
    current_num = e.get()
    # Deletes everything in the input field
    e.delete(0, END)
    # Gets the current input field value
    e.insert(0, str(current_num) + str(number))

def button_clear():
    # Deletes everything in the input field
    e.delete(0, END)

def button_add():
    # Gets the current input field value
    f_num = e.get()

    # global ---> If you want to use the variable outside the function
    global math
    math = "addition"
    global first_number
    first_number = int(f_num)

    # Deletes everything in the input field
    e.delete(0, END)

def button_subtract():
    # Gets the current input field value
    f_num = e.get()

    # global ---> If you want to use the variable outside the function
    global math
    math = "subtraction"
    global first_number
    first_number = int(f_num)

    # Deletes everything in the input field
    e.delete(0, END)

def button_multiply():
    # Gets the current input field value
    f_num = e.get()

    # global ---> If you want to use the variable outside the function
    global math
    math = "multiplication"
    global first_number
    first_number = int(f_num)

    # Deletes everything in the input field
    e.delete(0, END)
    
def button_divide():
    # Gets the current input field value
    f_num = e.get()

    # global ---> If you want to use the variable outside the function
    global math
    math = "division"
    global first_number
    first_number = int(f_num)

    # Deletes everything in the input field
    e.delete(0, END)

def button_equal():
    s_num = e.get()
    e.delete(0, END)
    
    match math:
        case "addition":
            e.insert(0, first_number + int(s_num))
        case "subtraction":
            e.insert(0, first_number - int(s_num))
        case "multiplication":
            e.insert(0, first_number * int(s_num))
        case "division":
            e.insert(0, first_number / int(s_num))

# Creating the buttons
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
buttonPlus = Button(root, text="+", padx=40, pady=20, command=button_add)
buttonMinus = Button(root, text="-", padx=40, pady=20, command=button_subtract)
buttonMultiply = Button(root, text="+", padx=40, pady=20, command=button_multiply)
buttonDivide = Button(root, text="/", padx=40, pady=20, command=button_divide)
buttonEqual = Button(root, text="=", padx=40, pady=20, command=button_equal)
buttonClear = Button(root, text="C", padx=40, pady=20, command=button_clear)

# Placing the buttons on the screen
button9.grid(row=1, column=1)
button8.grid(row=1, column=2)
button7.grid(row=1, column=3)
buttonPlus.grid(row=1, column=4)

button6.grid(row=2, column=1)
button5.grid(row=2, column=2)
button4.grid(row=2, column=3)
buttonMinus.grid(row=2, column=4)

button3.grid(row=3, column=1)
button2.grid(row=3, column=2)
button1.grid(row=3, column=3)
buttonMultiply.grid(row=3, column=4)

button0.grid(row=4, column=1)
buttonEqual.grid(row=4, column=2)
buttonClear.grid(row=4, column=3)
buttonDivide.grid(row=4, column=4)

root.mainloop()