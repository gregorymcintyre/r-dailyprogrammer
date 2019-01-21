'''
Have the function SimpleAdding(num) add up all the numbers from 1 to num. For example: if the input is 4 then your program should return 10 because 1 + 2 + 3 + 4 = 10. For the test cases, the parameter num will be any number from 1 to 1000. 
Codebytes
'''

from test import test

def SimpleAdding(num):
    if num <=1:
        return 1
    else:
        return num + SimpleAdding(num-1)


#print(SimpleAdding(4))
#print(SimpleAdding(12))
#print(SimpleAdding(140))

test(SimpleAdding, 10, 4)
test(SimpleAdding, 78, 12)
test(SimpleAdding, 9870, 140)
