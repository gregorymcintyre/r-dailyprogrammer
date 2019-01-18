'''
Have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word. Words will be separated by only one space. 

CodeBytes
'''
from test import test

def LetterCapitalize(str):
    output = list(str)
    for i, v in enumerate(output):
        if output[i-1]==' ' or i==0:
            output[i] = v.upper()
        
    return ''.join(output)

test(LetterCapitalize, "hello world", "Hello World")
test(LetterCapitalize, "i ran there", "I Ran There")
#print(LetterCapitalize(input()))
