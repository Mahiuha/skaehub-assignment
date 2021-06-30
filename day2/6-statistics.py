#import both the requests and json modules
import requests
import json

#url to pass 
url = 'https://infama-api.pacisvorgel.co.ke/public/api/links'

#outputs the json file
x =requests.get(url)
print(x.json())

with open("links.json", "w") as outfile:
    json.dump(x.json(), outfile)