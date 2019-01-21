'''
Have the function CheckNums(num1,num2) take both parameters being passed and return the string true if num2 is greater than num1, otherwise return the string false. If the parameter values are equal to each other then return the string -1.

Codebytes
'''

from test import test

def CheckNums(num1, num2):
    if num1 > num2:
        return False
    elif num1 < num2:
        return True
    else:
        return -1

'''
def test(func, outp, *inp):
    #print(func(*inp))
    if func(*inp) == outp:
        print('Pass')
    else:
        print('fail')
'''

#print(CheckNums(3, 122))
#print(CheckNums(67, 67))

test(CheckNums, True,  3, 122)
test(CheckNums, -1, 67, 67)


