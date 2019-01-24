'''
Have the function CorrectPath(str) read the str parameter being passed, which will represent the movements made in a 5x5 grid of cells starting from the top left position. The characters in the input string will be entirely composed of: r, l, u, d, ?. Each of the characters stand for the direction to take within the grid, for example: r = right, l = left, u = up, d = down. Your goal is to determine what characters the question marks should be in order for a path to be created to go from the top left of the grid all the way to the bottom right without touching previously travelled on cells in the grid.

For example: if str is "r?d?drdd" then your program should output the final correct string that will allow a path to be formed from the top left of a 5x5 grid to the bottom right. For this input, your program should therefore return the string rrdrdrdd. There will only ever be one correct path and there will always be at least one question mark within the input string.

CoderBytes
'''

from test import test

def CorrectPath(str):
    listPath = list(str)
    x = 4
    y = 4
    for step in listPath:
        if step == 'r':
            x -= 1
        elif step == 'd':
            y-= 1
        elif step == 'l':
            x+= 1
        elif step == 'u':
            y+= 1

    #print(x, y)
    #print(listPath)

    for step in range(len(listPath)):
        if listPath[step] == '?' and ((x ==0 and y == 0) or (y < 0)):
            listPath[step] = 'u'
            y += 1
        
        elif listPath[step] == '?' and y > 0:
            listPath[step] = 'd'
            y -= 1

        elif listPath[step] == '?' and x < 0:
            listPath[step] = 'r'
            x += 1
           
        elif listPath[step] == '?' and x > 0:
            listPath[step] = 'l'
            x -= 1

    #print(listPath)
    #print(x, y)

    return ''.join(listPath)

#print(CorrectPath("???rrurdr?"))        #dddrrurdrd
#print(CorrectPath("drdr??rrddd?"))      #drdruurrdddd

test(CorrectPath, 'dddrrurdrd', '???rrurdr?')
test(CorrectPath, 'drdruurrdddd', 'drdr??rrddd?')

