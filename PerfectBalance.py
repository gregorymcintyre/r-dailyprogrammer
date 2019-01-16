'''
https://www.reddit.com/r/dailyprogrammer/comments/afxxca/20190114_challenge_372_easy_perfectly_balanced/

Given a string containing only the characters x and y, find whether there are the same number of xs and ys.

'''

#input = input()

#print(input)

def balanced(input):
    x=0
    y=0
    
    for char in input:
        if char == 'x':
            x += 1
        elif char == 'y':
            y += 1
        else:
            print('end')
    #print('x = ' + str(x) + ', y = ' + str(y)) 
    print('balanced(\"' +  input + '\") => ', end=' ')

    if x == y:
        print('True')
        return True
    else:
        print('False')
        return False

balanced("xxxyyy")
balanced("yyyxxx")
balanced("xxxyyyy")
balanced("yyxyxxyxxyyyyxxxyxyx")
balanced("xyxxxxyyyxyxxyxxyy")
balanced("")
balanced("x")
