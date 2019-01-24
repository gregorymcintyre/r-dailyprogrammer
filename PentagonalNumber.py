'''
Have the function PentagonalNumber(num) read num which will be a positive integer and determine how many dots exist in a pentagonal shape around a center dot on the Nth iteration. For example, in the image below you can see that on the first iteration there is only a single dot, on the second iteration there are 6 dots, on the third there are 16 dots, and on the fourth there are 31 dots

https://en.wikipedia.org/wiki/Centered_pentagonal_number

1, 6, 16, 31, 51, 76, 106, 141, 181, 226, 276, 331, 391, 456, 526, 601, 681, 766, 856, 951, 1051, 1156, 1266, 1381, 1501, 1626, 1756, 1891, 2031, 2176, 2326, 2481, 2641, 2806, 2976

Coderbytes
'''

from test import test

def PentagonalNumber(num):
    base = 0
    output = 1
    for count in range(num):
        output += base
        base += 5
    
    return output

#print(PentagonalNumber(2))

test(PentagonalNumber, 6, 2)
test(PentagonalNumber, 51, 5)
test(PentagonalNumber, 31, 4)
