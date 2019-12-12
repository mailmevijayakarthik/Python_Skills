
from geopy.geocoders import ArcGIS
nom=ArcGIS()
n=nom.geocode("3995 23rd St, San Francisco , CA 94114")
print(n.latitude)
