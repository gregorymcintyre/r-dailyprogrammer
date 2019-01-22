'''
Have the function MaximalSquare(strArr) take the strArr parameter being passed which will be a 2D matrix of 0 and 1's, and determine the area of the largest square submatrix that contains all 1's. A square submatrix is one of equal width and height, and your program should return the area of the largest submatrix that contains only 1's. For example: if strArr is ["10100", "10111", "11111", "10010"] then this looks like the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

For the input above, you can see the bolded 1's create the largest square submatrix of size 2x2, so your program should return the area which is 4. You can assume the input will not be empty.

Hard challenges are worth 15 points and you are not timed for them. 


CodeBytes
'''

from test import test

def MaximalSquare(strArr):
    
    value = 0
    maxValue = 1
    offset = 0

    diagCount = len(strArr)


    for x in range(0, diagCount):
        for y in range(0, diagCount):
            if strArr[x][y] == 1:
                value += 1
                print(value)

    for base in range(0, diagCount):
        if value == base**2:
            if value > maxValue:
                maxValue == value
                print(value)

    diagCount -= 1
    offset += 1

    return maxValue

print(MaximalSquare([[0,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]))

#test(MaximalSquare, 9, [[0,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]])
