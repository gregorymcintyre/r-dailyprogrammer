'''
Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.

Codebytes
'''
from test import test

def LetterChanges(string):
    output_list = list(string)
    for pos, char in enumerate(output_list):    
        if char.isalpha():
            if char.lower()=='z':
                output_list[pos] = 'A'
            else:
                output_list[pos] = chr(ord(char)+1)
    
    for pos, char in enumerate(output_list):
        if char.lower() in 'aeiou':
            output_list[pos] = char.upper()

    return ''.join(output_list)

#test(LetterChanges, 'hello*3', "Ifmmp*3")
#test(LetterChanges, 'fun times!', "gvO Ujnft!")

test(LetterChanges, "Ifmmp*3", 'hello*3')
test(LetterChanges, "gvO Ujnft!", 'fun times!')

#print(LetterChanges(input()))
