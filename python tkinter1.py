from tkinter import*

root=Tk()
root.geometry('350x400')
Label(root,text="Red Sun",bg="red",fg="White").grid(row=0,column=0)
Label(root,text="Green Grass",bg="green",fg="black").grid(row=0,column=1)
Label(root,text="Blue Sky",bg="blue",fg="White").grid(row=0,column=2)

mainloop()