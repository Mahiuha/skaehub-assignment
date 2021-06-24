#import the numpy library
#prompt the user for the year
#prompt the user for the month
#print to the user the number of weekdays as output

import numpy as np

print('Enter From Day YYYY-MM e.g 2021-07')
start_count = input()
print('Enter To Day YYYY-MM e.g 2021-07')
stop_count = input()
s= np.busday_count(start_count, stop_count)

print(s)
