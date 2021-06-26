#importing the Nominatim API from geopy.geocoders library
from geopy.geocoders import Nominatim

#initializing the nominatim API
geolocator = Nominatim(user_agent='question3')

#reversing latitude and longitude back to location
location1 = geolocator.reverse("-1.3031689499999999, 36.826061224105075")
print(location1.address)