#importing the Nominatim API from geopy.geocoders library
from geopy.geocoders import Nominatim

#Initializing the nominatim API
geolocator = Nominatim(user_agent='question3')

#prompt user for latitude and longitude
user_lat = int(input()

#reversing given latitude and longitude to location
location1 = geolocator.reverse("-1.3031689499999999, 36.826061224105075")
print(location1.address)
