#importing modules and libraries
#nominatim is an API
#haversine is a formula for calculating distance between two locations
from geopy.geocoders import Nominatim
import haversine as hs
import math

#initialize the Nominatim
geolocator = Nominatim(user_agent="2-distance.py")

#this code retrives map data from the string
location1 = geolocator.geocode("Nairobi")
location2 = geolocator.geocode("Cairo")

#this gets specific lat and long
lat1 = location1.latitude
lon1 = location1.longitude
lat2 = location2.latitude
lon2 = location2.longitude

#calculates distance between loc1 and loc2
loc1 = (lat1, lon1)
loc2 = (lat2, lat1)
my_hs = hs.haversine(loc1, loc2)

#prints the distance as output
print(my_hs)
