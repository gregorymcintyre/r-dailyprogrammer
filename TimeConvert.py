'''
Have the function TimeConvert(num) take the num parameter being passed and return the number of hours and minutes the parameter converts to (ie. if num = 63 then the output should be 1:3). Separate the number of hours and minutes with a colon.

Coderbytes

'''

from test import test

def TimeConvert(int):
    return str(int//60) + ':' + str(int%60)

#print(TimeConvert(126))
#print(TimeConvert(45))
#print(TimeConvert(63))

test(TimeConvert, '2:6', 126)
test(TimeConvert, '0:45', 45)
test(TimeConvert, '1:3', 63)
