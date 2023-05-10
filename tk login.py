import tkinter

from tkinter import *
window =Tk()
window.title("login facebook")
tkinter.Label(text="user name").grid(row=0)
tkinter.Entry(window).grid(row=0,column=1)
tkinter.Label(window,text="password").grid(row=1)
tkinter.Entry(window).grid(row=1,column=1)


btn=Button(window,text="Log in",bg="blue",fg="white")
btn.grid(column=6,row=5)
window.mainloop()
