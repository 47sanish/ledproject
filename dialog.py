from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('message Box')
root.iconbitmap('E:/image/global.com')

def popup():
    #showinfo messagebox
messagebox.showinfo('This is my popup', 'Hello World')

Button(root, text='popup',command=popup).pack()

mainloop()
