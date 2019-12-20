from tkinter import *

window=Tk()

b1=Button(window,text="FirstName")
b1.grid(row=0,column=0)
b2=Button(window,text="LastName")
b2.grid(row=1,column=0)

b3=Button(window,text="Register")
b3.grid(row=2,column=1)

e1=Entry(window)
e1.grid(row=0,column=1)
e2=Entry(window)
e2.grid(row=1,column=1)


window.mainloop()
