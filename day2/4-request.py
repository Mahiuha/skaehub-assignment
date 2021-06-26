#import the requests module
import requests

#requests the web page from server
url = 'https://infama-api.pacisvorgel.co.ke/public/api/links'
key_value = {'mainurl': 'twitter.com'}

#raw socket response from server
x = requests.post(url, data = key_value)
print('Server Response Code:',x.status_code)
print(x.text)