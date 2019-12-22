"""
A program that stores Title , Author , Year , ISBN details

User can :
View All
Search Entry
Add Entry
Update Selected
Delete Selected
Close
"""

from tkinter import *
from Backend_usingOOPS import Database

database=Database()


def get_selected_row(event):
    try:
        global selected_tuple
        index=lb.curselection()[0]
        selected_tuple=lb.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass

def view_command():
    lb.delete(0,END)
    for row in database.view():
        lb.insert(END,row)

def Search_Entry():
    lb.delete(0,END)
    for row in database.search(title_value.get(),author_value.get(),year_value.get(),isbn_value.get()):
        lb.insert(END,row)

def Add_Entry():
    lb.delete(0,END)
    database.insert(title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    lb.insert(END,(title_value.get(), author_value.get(), year_value.get(), isbn_value.get()))


def Delete():
    database.delete(selected_tuple[0])
    view_command()

def Update_Entry():
    database.update(selected_tuple[0],title_value.get(),author_value.get(),year_value.get(),isbn_value.get())
    view_command()


def close():
    window.destroy()

window=Tk()
window.wm_title("Book Library")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)
l2=Label(window,text="Author")
l2.grid(row=0,column=2)
l3=Label(window,text="Year")
l3.grid(row=1,column=0)
l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_value=StringVar()
e1=Entry(window,textvariable=title_value)
e1.grid(row=0,column=1)
author_value=StringVar()
e2=Entry(window,textvariable=author_value)
e2.grid(row=0,column=3)
year_value=StringVar()
e3=Entry(window,textvariable=year_value)
e3.grid(row=1,column=1)
isbn_value=StringVar()
e4=Entry(window,textvariable=isbn_value)
e4.grid(row=1,column=3)

b1=Button(window,text="View All",height=1,width=20,command=view_command)
b1.grid(row=2,column=3)
b2=Button(window,text="Search Entry",height=1,width=20,command=Search_Entry)
b2.grid(row=3,column=3)
b3=Button(window,text="Add Entry",height=1,width=20,command=Add_Entry)
b3.grid(row=4,column=3)
b4=Button(window,text="Update Selected",height=1,width=20,command=Update_Entry)
b4.grid(row=5,column=3)
b5=Button(window,text="Delete Selected",height=1,width=20,command=Delete)
b5.grid(row=6,column=3)
b6=Button(window,text="Close",height=1,width=20,command=close)
b6.grid(row=7,column=3)

lb = Listbox(window,height=8,width=30)
lb.grid(row=2,column=0,rowspan=6,columnspan=2)

sb=Scrollbar(window)
sb.grid(row=2,column=2,rowspan=6,columnspan=1)

lb.bind('<<ListboxSelect>>',get_selected_row)

lb.configure(yscrollcommand=sb.set)
sb.configure(command=lb.yview)

window.mainloop()
