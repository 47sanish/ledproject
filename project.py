from tkinter import *
root = Tk()
e1 = Entry(root, width=50, fg="Red",bg="black", borderwidth=5)
e1.pack()

def myclick():
    textoutput= "ABHAY MUGI" + e1.get()

    myLabel = Label(root, text=textoutput)

    myLabel.pack()

myButton=Button(root, text="click Here", command=myclick)
myButton.pack()


root.mainloop()


