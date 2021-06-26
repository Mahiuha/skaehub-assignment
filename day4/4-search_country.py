#import nominatim API from the geopy.geocoders library
from geopy.geocoders import Nominatim

#initializes the Nominatim API 
geolocator = Nominatim(user_agent="question1")

#Prompt user to enter zip for Kenya one must add Town name then the zip code
entered_state = input("Enter a State or Town name: ")
print("\nCountry:",entered_state)

#Pass state to geolocator(nominatim) function
#geocode resolves a location from a string
location = geolocator.geocode(entered_state)
##print("Details of the said pincode:")
details = location.address

country = details.split(',')
print(country[-1])