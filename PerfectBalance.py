'''
https://www.reddit.com/r/dailyprogrammer/comments/afxxca/20190114_challenge_372_easy_perfectly_balanced/

Given a string containing only the characters x and y, find whether there are the same number of xs and ys.

'''
from test import test

def balanced(input):
    x=0
    y=0
    
    for char in input:
        if char == 'x':
            x += 1
        elif char == 'y':
            y += 1
            
    if x == y:
        return True
    else:
        return False

test(balanced, "xxxyyy", True)
test(balanced, "yyyxxx", True)
test(balanced, "xxxyyyy", False)
test(balanced, "yyxyxxyxxyyyyxxxyxyx", True)
test(balanced, "xyxxxxyyyxyxxyxxyy", False)
test(balanced, "", True)
test(balanced, "x", False)

