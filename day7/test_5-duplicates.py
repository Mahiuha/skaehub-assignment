import pytest
import duplicates

#test if duplicates are removed
def main(x):
    clean_list = duplicates.main(x)
    return clean_list

def test_main():
    assert main(['1','2','2','3']) == set(['1','2','3'])


#check if set has value
def is_set_has_values(x):
    clean_list = duplicates.list_length(x)
    return clean_list

def test_is_set_have_values():
    assert is_set_has_values(['1','22','3']) > 0

#check if set is empty
def is_set_empty(x):
    clean_list = duplicates.list_length(x)
    return clean_list

def test_is_set_empty():
    assert is_set_empty([]) == 0

# #checl if set is of type set
# def is_set_type_set(clean_list):
#     set_type = question5.set_type(clean_list)
#     return set_type

# def test_is_set_type_set():
#     assert is_set_type_set(['1']) == type(set)


      
