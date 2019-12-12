import folium

#/Users/vijayakarthikeyanarul/git/python_Skills/Application/Mapping
map=folium.Map(location=[29.5153413, -98.5632239])
map
map.save("Map1.html")
map2=folium.Map(location=[29.5153413, -98.5632239],zoom_start=8,tiles="Stamen Terrain")

fg=folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[29.5153413, -98.5632239],popup="Karthik is Here",icon=folium.Icon(color='red')))
fg.add_child(folium.Marker(location=[29.4405250, -98.4934850],popup="My Work",icon=folium.Icon(color='green')))
map2.add_child(fg)


map2.save("Our_Map.html")


#29.5153413, -98.5632239 Home
# 29.4405250, -98.4934850 Work