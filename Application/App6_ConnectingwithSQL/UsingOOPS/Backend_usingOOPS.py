import sqlite3

class Database:
    def __init__(self):
        self.conn=sqlite3.connect("book.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE if not Exists book (id INTEGER PRIMARY KEY, title TEXT,author TEXT,year INTEGER,isbn INTEGER)")


    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT*FROM book")
        records=self.cur.fetchall()
        return records

    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT*FROM book WHERE title=? or author=? or year =? or isbn = ?",(title,author,year,isbn))
        records = self.cur.fetchall()
        return records

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?", (title,author,year,isbn,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

#insert("Power is great","Kar",2009,34334342323343)
#print(search("Power","","",""))
#delete(4)
#print(view())
#update(2,"SUN","Arul",2010,23242442)
#print(view())