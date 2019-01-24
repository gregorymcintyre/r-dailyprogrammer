'''
Have the function KaprekarsConstant(num) take the num parameter being passed which will be a 4-digit number with at least two distinct digits. Your program should perform the following routine on the number: Arrange the digits in descending order and in ascending order (adding zeroes to fit it to a 4-digit number), and subtract the smaller number from the bigger number. Then repeat the previous step. Performing this routine will always cause you to reach a fixed number: 6174. Then performing the routine on 6174 will always give you 6174 (7641 - 1467 = 6174). Your program should return the number of times this routine must be performed until 6174 is reached. For example: if num is 3524 your program should return 3 because of the following steps: (1) 5432 - 2345 = 3087, (2) 8730 - 0378 = 8352, (3) 8532 - 2358 = 6174.

Coderbytes
'''

from test import test

def KaprekarsConstant(num):

    if len(str(num))<4:
        num = num*10**(4-len(str(num)))

    ascList = list(map(str, str(num)))
    desList = list(map(str, str(num)))
    ascList.sort()
    desList.sort(reverse=True)
    number = int(''.join(desList)) - int(''.join(ascList))
#    print(number)
    
    if number == 6174:
        return 1
    else:
        return 1 + KaprekarsConstant(number)


#print(KaprekarsConstant(9831))
#print(KaprekarsConstant(2111))
#print(KaprekarsConstant(3524))
#print(KaprekarsConstant(1))
#print(KaprekarsConstant(9998))

test(KaprekarsConstant, 7, 9831)
test(KaprekarsConstant, 5, 2111)
test(KaprekarsConstant, 3, 3524)

