# import statistics module
import statistics

list_one = [1,2,3,4,5,6,7,8,9,10]

print("The average of values in list_one is {}".format(statistics.mean(list_one)))

print("The median of values in list_one is {}".format(statistics.median(list_one)))

print("The mode of values in list_one is {}".format(statistics.mode(list_one)))

print("The variance of values in list_one is {}".format(statistics.variance(list_one)))
# #import both the requests and json modules
# import requests
# import json

# #url to pass 
# url = 'https://infama-api.pacisvorgel.co.ke/public/api/links'

# #outputs the json file
# x =requests.get(url)
# print(x.json())

# with open("links.json", "w") as outfile:
#     json.dump(x.json(), outfile)