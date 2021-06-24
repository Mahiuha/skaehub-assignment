#import the libraries
#here we compute the dates
#then display to the user the dates as output
import numpy as np

today = np.datetime64('today', 'D')
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')

print('The date today is: ', today)
print('The date yesterday was: ', yesterday)
print('The date tmorrow will be: ', tomorrow)