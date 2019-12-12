
import time
import os

while True:
    if os.path.exists("fruits.txt"):
        with open("fruits.txt","r") as myfile:
            content=myfile.read()
            print(content)
    else:
        with open("fruits.txt","x") as myfile:
            print("New file created ...")
            myfile.write("Apple")

    time.sleep(2)