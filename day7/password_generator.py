#password
#create list 
#shuffle items in list
#print new order list
#select first 7 items as password

import random

 

s = ['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','~','!','@','$','*','%','`','?','[',']',';','<','>','?','.','-','(',')','a','b','c','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

e = ['a','b','c','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

m = ['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

random.shuffle(m)
random.shuffle(s)
random.shuffle(e)

def randomize(m):
    shuffled_m= random.shuffle(m)
    return shuffled_m

        #print("List after first shuffle:", s)

    # Python program to convert a list
    # to string using join() function
        
    # Function to convert  

def listToString(s): 
        
        # initialize an empty string
    strong_password = "" 
    print(listToString(s)) 
        # return string  
    return strong_password.join(s)

        # preview result    
        


def listToString(e): 
    easy_password = "" 
    return (easy_password.join(e))



def listToString(m): 
    medium_password = "" 
    return (medium_password.join(m))


def main(strength):
    
    if (strength == 'm'):
        truncated_text = listToString(m)[:10]
        return truncated_text
    elif(strength == 'e'):
        truncated_text = listToString(e)[:7]
        return truncated_text
    elif(strength == 's'):
        truncated_text = listToString(s)[:15]  
        return truncated_text  
    else:
        truncated_text = 'invalid text'
        return truncated_text


      
main('e')