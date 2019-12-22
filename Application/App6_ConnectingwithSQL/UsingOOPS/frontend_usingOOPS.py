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

database=Database("book.db")

class Window(object):
    def __init__(self,window):

        self.window=window
        window.wm_title("Book Library")

        l1 = Label(window, text="Title")
        l1.grid(row=0, column=0)
        l2 = Label(window, text="Author")
        l2.grid(row=0, column=2)
        l3 = Label(window, text="Year")
        l3.grid(row=1, column=0)
        l4 = Label(window, text="ISBN")
        l4.grid(row=1, column=2)

        self.title_value = StringVar()
        self.e1 = Entry(window, textvariable=self.title_value)
        self.e1.grid(row=0, column=1)
        self.author_value = StringVar()
        self.e2 = Entry(window, textvariable=self.author_value)
        self.e2.grid(row=0, column=3)
        self.year_value = StringVar()
        self.e3 = Entry(window, textvariable=self.year_value)
        self.e3.grid(row=1, column=1)
        self.isbn_value = StringVar()
        self.e4 = Entry(window, textvariable=self.isbn_value)
        self.e4.grid(row=1, column=3)

        b1 = Button(window, text="View All", height=1, width=20, command=self.view_command)
        b1.grid(row=2, column=3)
        b2 = Button(window, text="Search Entry", height=1, width=20, command=self.Search_Entry)
        b2.grid(row=3, column=3)
        b3 = Button(window, text="Add Entry", height=1, width=20, command=self.Add_Entry)
        b3.grid(row=4, column=3)
        b4 = Button(window, text="Update Selected", height=1, width=20, command=self.Update_Entry)
        b4.grid(row=5, column=3)
        b5 = Button(window, text="Delete Selected", height=1, width=20, command=self.Delete)
        b5.grid(row=6, column=3)
        b6 = Button(window, text="Close", height=1, width=20, command=self.close)
        b6.grid(row=7, column=3)

        self.lb = Listbox(window, height=8, width=30)
        self.lb.grid(row=2, column=0, rowspan=6, columnspan=2)

        sb = Scrollbar(window)
        sb.grid(row=2, column=2, rowspan=6, columnspan=1)

        self.lb.bind('<<ListboxSelect>>', self.get_selected_row)

        self.lb.configure(yscrollcommand=sb.set)
        sb.configure(command=self.lb.yview)


    def get_selected_row(self,event):
        try:

            index=self.lb.curselection()[0]
            self.selected_tuple=self.lb.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END, self.selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END, self.selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END, self.selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        self.lb.delete(0,END)
        for row in database.view():
            self.lb.insert(END,row)

    def Search_Entry(self):
        self.lb.delete(0,END)
        for row in database.search(self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get()):
            self.lb.insert(END,row)

    def Add_Entry(self):
        self.lb.delete(0,END)
        database.insert(self.title_value.get(), self.author_value.get(), self.year_value.get(), self.isbn_value.get())
        self.lb.insert(END,(self.title_value.get(), self.author_value.get(), self.year_value.get(), self.isbn_value.get()))


    def Delete(self):
        database.delete(self.selected_tuple[0])
        self.view_command()

    def Update_Entry(self):
        database.update(self.selected_tuple[0],self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get())
        self.view_command()


    def close(self):
        window.destroy()


window=Tk()
Window(window)
window.mainloop()
