import sqlite3

def CreateConnection():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE if not Exists book (id INTEGER PRIMARY KEY, title TEXT,author TEXT,year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT*FROM book")
    records=cur.fetchall()
    conn.close()
    return records

def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT*FROM book WHERE title=? or author=? or year =? or isbn = ?",(title,author,year,isbn))
    records = cur.fetchall()
    conn.close()
    return records

def delete(id):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?", (title,author,year,isbn,id))
    conn.commit()
    conn.close()



CreateConnection()
#insert("Power is great","Kar",2009,34334342323343)
#print(search("Power","","",""))
#delete(4)
#print(view())
#update(2,"SUN","Arul",2010,23242442)
#print(view())