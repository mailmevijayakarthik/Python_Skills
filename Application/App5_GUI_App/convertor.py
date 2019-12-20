from tkinter import *

window=Tk()

def km_to_miles():
    t1.delete('1.0', END)
    try :
        miles = float(e1_value.get()) * 1.6
    except ValueError:
        miles = "INVALID"
    t1.insert(END,miles)

def closeEverything():
    window.destroy()

b1=Button(window,text="Execute",command=km_to_miles)
b1.grid(row=0,column=0)

b2=Button(window,text="Close",command=closeEverything)
b2.grid(row=0,column=3)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)

window.mainloop()
