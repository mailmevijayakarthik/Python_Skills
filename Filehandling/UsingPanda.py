
import time
import os
import pandas


if os.path.exists("/Users/vijayakarthikeyanarul/git/python_Skills/Filehandling/temp_calculation.csv"):
    data=pandas.read_csv("/Users/vijayakarthikeyanarul/git/python_Skills/Filehandling/temp_calculation.csv")
    print(data)
    print(data.mean()["Column2"])
    print(data.mode())
else:
    print("File not present")