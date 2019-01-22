'''
Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it. For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. For the test cases, the range will be between 1 and 18 and the input will always be an integer. 

Coderbytes
'''

from test import test

def FirstFactorial(num):
    if num == 1:
        return 1
    else:
        num *= FirstFactorial(num - 1)
    
    return num

#print(FirstFactorial(4))
#print(FirstFactorial(8))

test(FirstFactorial, 24, 4)
test(FirstFactorial, 40320, 8)

