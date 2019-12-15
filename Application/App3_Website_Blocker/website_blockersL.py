import time
from  datetime import datetime as dt
host_temp="hosts"
hostpath="/etc/hosts"
redirtect="127.0.0.1"
websites=["www.facebook.com","www.linkedin.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,20):
        print("Its working Hour. Blocking all Social Media")
        with open(hostpath,"r+") as file:
            content=file.read()
            for sites in websites:
                if sites in content:
                    pass
                else:
                    file.write(redirtect+" "+sites+"\n")

    else:

        with open(hostpath, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(sites in line for sites in websites):
                    file.write(line)
            file.truncate()
        print("I am offline !!! Allowing Social Media Access")
    time.sleep(2)
