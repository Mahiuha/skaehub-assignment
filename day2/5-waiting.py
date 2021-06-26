#import the requests module
import requests

#prompt user to input the delay time in seconds for response
seconds = float(input("Enter number of seconds: "))

try:
    url = 'https://infama-api.pacisvorgel.co.ke/public/api/links'
    #response from server
    x =requests.get(url, timeout = seconds)
    print('Server Response Code:',x.status_code)
    print(x.text)
#timeout error
except requests.exceptions.RequestException as e:
    print(e)   