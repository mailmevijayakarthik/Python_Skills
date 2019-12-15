import folium
import pandas

data=pandas.read_csv("Volcanoes.csv")

lat=list(data["LAT"])
long=list(data["LON"])
name=list(data["NAME"])
elev=list(data["ELEV"])

map=folium.Map(location=[29.5153413, -98.563223],zoom_start=6,titles="Stamen Terrain")
def colorProdcurer(elev):
    if elev <1000:
        return 'green'
    elif 1000<=elev<3000 :
        return 'orange'
    else :
        return 'red'


fg=folium.FeatureGroup(name="Karthik's World")
fg.add_child(folium.Marker(location=[29.5153413, -98.5632239],popup="Karthik is Here",icon=folium.Icon(color='red')))
fg.add_child(folium.Marker(location=[29.4405250, -98.4934850],popup="My Work",icon=folium.Icon(color='green')))

fg1=folium.FeatureGroup(name="My Must See Spots")
for lt,lng,name,el in zip(lat,long,name,elev):
    fg1.add_child(folium.CircleMarker(location=[lt,lng],popup=str(el)+" m",radius=6,fill_color=colorProdcurer(el),color='grey',fill_opacity=0.7))
# we can use Circle Mark to make a circle

fgp=folium.FeatureGroup(name="World Population Map")
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'yellow' if x['properties']['POP2005']<10000000 else 'orange' if 10000000<=x['properties']['POP2005']<=20000000 else 'red'}))

map.add_child(fg)
map.add_child(fg1)
map.add_child(fgp)
map.add_child(folium.LayerControl())


map.save("Our_Map.html")


#29.5153413, -98.5632239 Home
# 29.4405250, -98.4934850 Work