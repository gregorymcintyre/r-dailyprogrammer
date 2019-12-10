'''
[2019-02-11] Challenge #375 [Easy] Print a new number by adding one to each of its digit
Description
A number is input in computer then a new no should get printed by adding one to each of its digit. If you encounter a 9, insert a 10 (don't carry over, just shift things around).

For example, 998 becomes 10109.

Bonus
This challenge is trivial to do if you map it to a string to iterate over the input, operate, and then cast it back. Instead, try doing it without casting it as a string at any point, keep it numeric (int, float if you need it) only.

Credit
This challenge was suggested by user /u/chetvishal, many thanks! If you have a challenge idea please share it in r/dailyprogrammer_ideas and there's a good chance we'll use it.

https://www.reddit.com/r/dailyprogrammer/comments/aphavc/20190211_challenge_375_easy_print_a_new_number_by/
'''

import math

def PrintNewAddingOne (num):
    intString = str(num)
    resultString = ""
    
    #print(intString)
    for c in intString:
        resultString += str(int(c)+1)

    print(resultString)
    
    return intString

def PrintNewAddingOneBonus (num):
    #print (int(math.log10(num))+1)
    #print(num)
    count=1
    result = 0
    power = 0
    
    for x in range (int(math.log10(num))+1):
        digit = ((num // count % 10)+1)
        result += digit*(10**power)
        #print("#" + str(digit))
        #print(10**power)
        if digit == 10:
            power = power +2
        else:
            power = power +1
        count = count *10
    
    print(result)
    return result


PrintNewAddingOne(998)
PrintNewAddingOneBonus(998)