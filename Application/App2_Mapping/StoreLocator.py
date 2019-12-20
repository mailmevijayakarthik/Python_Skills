import pandas
import folium

from geopy.geocoders import ArcGIS
import time

data=pandas.read_csv("entry.csv")
lat=list(data["Latitude"])
long=list(data["Longitude"])
name=list(data["STORE_NAME"])

map=folium.Map(location=[29.5153413, -98.563223],zoom_start=2,titles="Mapbox")
fg=folium.FeatureGroup(name="My World")
fg.add_child(folium.Marker(location=[29.5153413, -98.5632239],popup="Karthik is Here",icon=folium.Icon(color='red')))
fg.add_child(folium.Marker(location=[29.4405250, -98.4934850],popup="My Work",icon=folium.Icon(color='green')))

fg1=folium.FeatureGroup(name="Favorate Shops for Grocery")
for lt,lng,name in zip(lat,long,name):
    fg1.add_child(folium.Marker(location=[lt,lng],popup=str(name),icon=folium.Icon(color='orange')))

map.add_child(fg)
map.add_child(fg1)
map.add_child(folium.LayerControl())
map.save("Fav_stores.html")


