import pandas
from geopy.geocoders import ArcGIS
import time

geolocator = ArcGIS(user_agent="StoreLocator",timeout=100)
location = geolocator.geocode("11521 NORTH FM620, BUILDING A AUSTIN TX")
#print(location.address)
#print((location.latitude, location.longitude))

def getLatLong(name,location):
        loc = geolocator.geocode(location)

        #myfile.write(mydetails)
        print(name,loc.address,loc.latitude,loc.longitude)

        return name,loc.latitude,loc.longitude




df1=pandas.read_excel("curbside_store_list.xlsx")

df1["Location"]=df1["ADDRESS_1"]+" "+df1["CITY"]+" "+ df1["STATE"]
df2=df1.drop(df1.columns[2:7],1)
df2["Coordinates"]=df2["Location"].apply(geolocator.geocode)
df2["Latitude"]=df2["Coordinates"].apply(lambda x:x.latitude if x!=None else None)
df2["Longitude"]=df2["Coordinates"].apply(lambda x:x.longitude if x!=None else None)


df2.to_csv(r'entry.txt',header=True,index=True,mode='a')


