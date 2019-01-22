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
    cache = strArr
    for x in range(len(strArr)):
        for y in range(len(strArr[0])):
            if cache[x][y] != 0 and x > 0 and y > 0:
                cache[x][y] += min(cache[x-1][y-1], cache[x-1][y], cache[x][y-1])
                #print(min(cache[x-1][y-1], cache[x-1][y], cache[x][y-1]))
    #print(cache)
    #print(max(max(cache)))
    return max(max(cache))**2

#print(MaximalSquare([[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]))
#print(MaximalSquare([[0,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]))
#print(MaximalSquare([[0,1,1,1], [1,1,0,1], [0,1,1,1]]))

test(MaximalSquare, 4, [[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]])
test(MaximalSquare, 9, [[0,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]])
test(MaximalSquare, 1, [[0,1,1,1], [1,1,0,1], [0,1,1,1]])

