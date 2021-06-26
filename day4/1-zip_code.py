#import the geopy library
#prompt user to input zip code.

from geopy.geocoders import Nominatim

#initialize  nominatim
geolocator = Nominatim(user_agent="1-zip_code.py")

#Prompt user to enter zip code, to be specific one must add country name then the zip code
zipcode = input("Enter zip code e.g kenya 00502: ")
print("\nZipcode:",zipcode)

#Pass zipcode to geolocator(nominatim) function
#geocode resolves a location from a string
location = geolocator.geocode(zipcode)
print("Details of the said pincode:")
print(location.address)

details = location.address

country = details.split(',')
print(country[-1])