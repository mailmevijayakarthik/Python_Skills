import mysql.connector

con=mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)


def wordInput():
    word = input("Enter the word:")

    return word

def query(word):
    cursor = con.cursor()
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression='%s'" % word)
    results = cursor.fetchall()
    return results


def searchword(word):
    results=query(word)
    if results:
        for result in results:
            print(result[1])
    else:
        print("No Result")

while True:
    word = wordInput()
    searchword(word)








