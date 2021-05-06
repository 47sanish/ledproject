from _ast import Lambda
from tkinter import *

root = Tk()

# defining title of the project
root.title("Simple calculator")

e = Entry(root, width=35, borderwidth=5)
e.gridth(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = e. get()
    e.delete(0, END)
    e.insert(0, str(current)  +  str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(second_number))

#defining the button
button_1 = Button(root, text="1", padax=40, pady=20, command=lambda : button_click(1))
button_2 = Button(root, text="2", padax=40, pady=20, command=lambda : button_click(2))
button_3 = Button(root, text="3", padax=40, pady=20, command=lambda : button_click(3))
button_4 = Button(root, text="4", padax=40, pady=20, command=lambda : button_click(4))
button_5 = Button(root, text="5", padax=40, pady=20, command=lambda : button_click(5))
button_6 = Button(root, text="6", padax=40, pady=20, command=lambda : button_click(6))
button_7 = Button(root, text="7", padax=40, pady=20, command=lambda : button_click(7))
button_8 = Button(root, text="8", padax=40, pady=20, command=lambda : button_click(8))
button_9 = Button(root, text="9", padax=40, pady=20, command=lambda : button_click(9))
button_0 = Button(root, text="0", padax=40, pady=20, command=lambda : button_click(0))
button_add = Button(root, text="clear", padx=79, pady=20, command=button_add)
button_equal = Button(root, text="clear", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="clear", padx=79, pady=20, command=button_clear)

#putting button on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4 , column=1, columnspan=2)
button_clear.grid(row=5, column=0)
button_equal.grid(row=5 , column=1, columnspan=2)

root.mainloop()