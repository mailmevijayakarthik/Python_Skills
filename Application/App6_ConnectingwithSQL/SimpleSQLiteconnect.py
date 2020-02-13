import sqlite3



def createTable():
    conn=sqlite3.connect("lite.db")
    curs=conn.cursor()
    curs.execute("CREATE TABLE if not Exists Store (item TEXT,quantity INTEGER,price REAL)")
    conn.commit()
    conn.close()

def insertItem(item,quantity,price):
    conn = sqlite3.connect("lite.db")
    curs = conn.cursor()
    curs.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

def viewItems():
    conn = sqlite3.connect("lite.db")
    curs = conn.cursor()
    curs.execute("SELECT * FROM Store")
    rows=curs.fetchall()
    conn.close()
    return rows

def deleteItem(item):
    conn = sqlite3.connect("lite.db")
    curs = conn.cursor()
    curs.execute("DELETE FROM Store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def updateItem(quantity,price,item):
    conn = sqlite3.connect("lite.db")
    curs = conn.cursor()
    curs.execute("UPDATE Store SET quantity=? ,price=? WHERE item=?", (quantity,price,item))
    conn.commit()
    conn.close()

def DeleteTable():
    conn = sqlite3.connect("lite.db")
    curs = conn.cursor()
    curs.execute("DROP TABLE Store")
    conn.commit()
    conn.close()

createTable()
insertItem("plates",5,20)
insertItem("Table",5,2000)
insertItem("chair",10,300)
insertItem("spoon",8,50)
print(viewItems())
deleteItem("Table")
print(viewItems())
updateItem(500,1000,"spoon")
print(viewItems())
#DeleteTable()

