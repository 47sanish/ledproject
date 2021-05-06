from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("check Box")
root.iconbitnep('E:/image/globel.ico')

def show():
    mylabel = Label(root, text=var.get()).pack()

Var = Stringvar()
#anything can be written in on or off string input
checkButton = checkButton(root, text="check this box!",
                          variable = var, onvalue="On",
                          offvalue="Off")
#Autonation selection on check box will be removed
checkButton.deselect()
checkButton.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

mainloop()