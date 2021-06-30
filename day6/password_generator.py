#import random module 
#prompt user for the password
#check if the password is comprises of lowercase, uppercase letters and symbols then print strong password
#if the password does not meet the strong password requirements go ahead and print weak password

import random


def password():
    user_input = input("Type strong or fair: ")

    if user_input.lower() == 'fair':
        return random.choice(['name123', 'pass12', 'memyself'])
    else:
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_)(*&^%$%#@!~?'
        password = ''.join(random.choices(letters, k=(random.randrange(8,24))))
        return password

print(password())



