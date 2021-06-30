import pytest
import csv_to_dictionary

#if file extension is detected
def is_file_extension_found(x):
    file_extension = csv_to_dictionary.file_extension(x)
    return file_extension  

def test_is_file_extension_found():
    assert is_file_extension_found('test.csv') == 'csv'


#test if file is has been uploaded
def is_file_uploaded(x):
    file_upload = csv_to_dictionary.file_not_uploaded(x)
    return file_upload

def test_is_file_uploaded():
    assert is_file_uploaded('text.csv') == "file uploaded"

#test if file is not uploaded
def is_file_is_not_uploaded(x):
    file_upload = csv_to_dictionary.file_not_uploaded(x)
    return file_upload

def test_is_file_is_not_uploaded():
    assert is_file_is_not_uploaded('') == "file not found"



