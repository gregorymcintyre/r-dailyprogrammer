'''
Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH. 


from Codebytes
'''
from test import test

def FirstReverse(string):
    return string[::-1]

#test(FirstReverse, "Hello World and Coders", 'sredoC dna dlroW olleH')
#test(FirstReverse, "coderbyte", "etybredoc")
#test(FirstReverse, "I Love Code", "edoC evoL I")

test(FirstReverse, 'sredoC dna dlroW olleH', "Hello World and Coders")
test(FirstReverse, "etybredoc", "coderbyte")
test(FirstReverse, "edoC evoL I", "I Love Code")

#print(FirstReverse(input()))

