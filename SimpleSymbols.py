'''
Have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an acceptable sequence by either returning the string true or false. The str parameter will be composed of + and = symbols with several letters between them (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol. So the string to the left would be false. The string will not be empty and will have at least one letter. 

Coderbytes
'''

from test import test

def SimpleSymbols(str):
    if str[0].isalpha() or str[-1].isalpha():           #quick check of first and last number
        return False
    for char in str[1:-1]:                              #ignore first and last(checked already)
        #print(char)
        if char.isalpha() and (str[str.index(char)-1] != '+' or str[str.index(char)+1] != '+'):         #using str[index] saves messing around with enumeration
            return False                                #is a letter, does not have + = fail 
    return True
    
#print(SimpleSymbols("++d+===+c++==a"))
#print(SimpleSymbols("+d+=3=+s+"))
#print(SimpleSymbols("f++d+"))

test(SimpleSymbols, False, "++d+===+c++==a")
test(SimpleSymbols, True, "+d+=3=+s+")
test(SimpleSymbols, False, "+d+=3=s+")
test(SimpleSymbols, False, "f++d+")









