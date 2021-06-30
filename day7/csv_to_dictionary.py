import csv

#specify the encoding type  utf-8 or iso-8859-1 to avoid the error
#UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc8
def file_extension(x):
    x = "file.csv"
    file_extension = x.split('.')
    file_ext = file_extension[-1]
    file_not_uploaded(x)
    return file_ext
    

def file_not_uploaded(x):
    y = len(x)
    if (y == 0):
        empty = "file not found"
        return empty
    else:
        file_uploaded ="file uploaded"
        return file_uploaded
    



def main():
    with open("file.csv", 'r', encoding="ISO-8859-1") as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            return dict(row)




