'''
UPC Check Digits

https://www.reddit.com/r/dailyprogrammer/comments/a72sdj/20181217_challenge_370_easy_upc_check_digits/

[2018-12-17] Challenge #370 [Easy] UPC check digits

The Universal Product Code (UPC-A) is a bar code used in many parts of the world. The bars encode a 12-digit number used to identify a product for sale, for example:

042100005264

The 12th digit (4 in this case) is a redundant check digit, used to catch errors. Using some simple calculations, a scanner can determine, given the first 11 digits, what the check digit must be for a valid code. (Check digits have previously appeared in this subreddit: see Intermediate 30 and Easy 197.) UPC's check digit is calculated as follows (taken from Wikipedia):

    Sum the digits at odd-numbered positions (1st, 3rd, 5th, ..., 11th). If you use 0-based indexing, this is the even-numbered positions (0th, 2nd, 4th, ... 10th).

    Multiply the result from step 1 by 3.

    Take the sum of digits at even-numbered positions (2nd, 4th, 6th, ..., 10th) in the original number, and add this sum to the result from step 2.

    Find the result from step 3 modulo 10 (i.e. the remainder, when divided by 10) and call it M.

    If M is 0, then the check digit is 0; otherwise the check digit is 10 - M.

For example, given the first 11 digits of a UPC 03600029145, you can compute the check digit like this:

    Sum the odd-numbered digits (0 + 6 + 0 + 2 + 1 + 5 = 14).

    Multiply the result by 3 (14 × 3 = 42).

    Add the even-numbered digits (42 + (3 + 0 + 0 + 9 + 4) = 58).

    Find the result modulo 10 (58 divided by 10 is 5 remainder 8, so M = 8).

    If M is not 0, subtract M from 10 to get the check digit (10 - M = 10 - 8 = 2).

So the check digit is 2, and the complete UPC is 036000291452.

Challenge

Given an 11-digit number, find the 12th digit that would make a valid UPC. You may treat the input as a string if you prefer, whatever is more convenient. If you treat it as a number, you may need to consider the case of leading 0's to get up to 11 digits. That is, an input of 12345 would correspond to a UPC start of 00000012345.

'''
from test import test

def upc(number):
    if len(str(number)) > 11:
        print('Code is too long')
   
    s_number=str(number)
    
    #Iterate backwards to avoid having to build into 11 str (starts at -1 the first digit, -2 second digit)
    odd = sum(int(i) for i in s_number[::-2])
    even =sum(int(i) for i in s_number[-2::-2])  

    code=(odd*3+even)%10
    if code!=0:
        code=10-code

    return code

test(upc, 4210000526, 4)
test(upc, 3600029145, 2)
test(upc, 12345678910, 4)
test(upc, 1234567, 0)

