#Enter Statement
#Split the explode (split) the statement
#select last item in array
#get string length of last item

def word_length(statement):
    empty_string(statement)
    x = statement.split()
    last_word = x[-1]
    return len(last_word)


#check if string is
def empty_string(x):
    y = len(x)
    if (y == 0):
        empty = "empty string"
        return y
    else:
        empty = "string is not empty"
        return empty




word_length('Django is a good dog')
