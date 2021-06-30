#create list


#test if list is empty

def main(x):
    #convert list to set
    clean_list = set(x)
    return clean_list


def list_length(clean_list):
    x = len(clean_list)
    return x

def set_type(clean_list):
    return  type(clean_list)  



main(['1','2','2','4'])