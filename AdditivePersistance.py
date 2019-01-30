'''
calculate the additive persistence of a number, defined as how many loops you have to do summing its digits until you get a single digit number. Take an integer N:

    Add its digits

    Repeat until the result has 1 digit

The total number of iterations is the additive persistence of N.

Your challenge today is to implement a function that calculates the additive persistence of a number.

https://www.reddit.com/r/dailyprogrammer/comments/akv6z4/20190128_challenge_374_easy_additive_persistence/


Bonus

The really easy solution manipulates the input to convert the number to a string and iterate over it. Try it without making the number a strong, decomposing it into digits while keeping it a number.

On some platforms and languages, if you try and find ever larger persistence values you'll quickly learn about your platform's big integer interfaces (e.g. 64 bit numbers)


Beautiful solution - u/k3rri6or

def add_persistence(n,t=1):
    s = 0
    while n:
        s += n % 10
        n //= 10
    
    if s >= 10:
         t += add_persistence(s,t)
    return t



'''

from test import test

def AdditivePersistence(number):
    cycles = 0
    
    while True:
        value = 0
        for digit in map(int, str(number)):
            value += digit
        if value > 9:
            cycles += 1
            number = value
        else:
            cycles += 1
            return cycles

#print(AdditivePersistence(13))
#print(AdditivePersistence(1234))
#print(AdditivePersistence(9876))
#print(AdditivePersistence(199))

test(AdditivePersistence, 1, 13)
test(AdditivePersistence, 2, 1234)
test(AdditivePersistence, 2, 9876)
test(AdditivePersistence, 3, 199)


