'''
Have the function AlphabetSoup(str) take the str string parameter being passed and return the string with the letters in alphabetical order (ie. hello becomes ehllo). Assume numbers and punctuation symbols will not be included in the string.

Codebytes
'''

from test import test

def AlphabetSoup(str):
    return ''.join(sorted(list(str)))

#print(AlphabetSoup("coderbyte"))

test(AlphabetSoup, "bcdeeorty", "coderbyte")
test(AlphabetSoup, "ahhloop", "hooplah")
