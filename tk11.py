import tkinter

from tkinter import *
window =Tk()
window.geometry('350x400')
tkinter.Label(window, text = "Name").grid(row = 0)
tkinter.Entry(window).grid(row = 0, column = 1)
tkinter.Label(window, text = "Father Name").grid(row = 1) 
tkinter.Entry(window).grid(row = 1, column = 1) 
tkinter.Label(window, text = "Mother Name").grid(row = 2)
tkinter.Entry(window).grid(row = 2, column = 1)


tkinter.Label(window, text = "Address").grid(row = 3)
tkinter.Text(window, width=20,height=5).grid(row=3,column=1)


lbl=Label(window,text="Gender")
lbl.grid(column=0,row=4)
rad1 = Radiobutton(window,text='Male', value=1)

rad2 = Radiobutton(window,text='Female', value=2)

rad3 = Radiobutton(window,text='Other', value=3)

rad1.grid(column=1, row=4)

rad2.grid(column=2, row=4)

rad3.grid(column=3, row=4)


lbl=Label(window,text="Language Known")
lbl.grid(column=0,row=7)
ch1=Checkbutton(window,text='Malayalam')
ch2=Checkbutton(window,text='English')
ch3=Checkbutton(window,text='Hindi')
ch1.grid(column=1, row=7)

ch2.grid(column=2, row=7)

ch3.grid(column=3, row=7)



btn=Button(window,text="Cancel",bg="black",fg="white")
btn.grid(column=6,row=11)
btn=Button(window,text="Submit",bg="black",fg="white")
btn.grid(column=12,row=11)


window.mainloop()
