import tkinter
from tkinter import messagebox

top = tkinter.Tk()
def hello():
   messagebox.showinfo("Say Hello", "Hello World")

B1 = tkinter.Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()
