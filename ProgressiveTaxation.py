'''
[2019-07-15] Challenge #379 [Easy] Progressive taxation
Challenge
The nation of Examplania has the following income tax brackets:

income cap      marginal tax rate
 10,000           0.00 (0%)
 30,000           0.10 (10%)
 100,000           0.25 (25%)
    --              0.40 (40%)
If you're not familiar with how tax brackets work, see the section below for an explanation.

Given a whole-number income amount up to 100,000,000, find the amount of tax owed in Examplania. Round down to a whole number of.

Examples
tax(0) => 0
tax(10000) => 0
tax(10009) => 0
tax(10010) => 1
tax(12000) => 200
tax(56789) => 8697
tax(1234567) => 473326

Optional improvement
One way to improve your code is to make it easy to swap out different tax brackets, for instance by having the table in an input file. If you do this, you may assume that both the income caps and marginal tax rates are in increasing order, the highest bracket has no income cap, and all tax rates are whole numbers of percent (no more than two decimal places).

However, because this is an Easy challenge, this part is optional, and you may hard code the tax brackets if you wish.

How tax brackets work
A tax bracket is a range of income based on the income caps, and each tax bracket has a corresponding marginal tax rate, which applies to income within the bracket. In our example, the tax bracket for the range 10,000 to 30,000 has a marginal tax rate of 10%. Here's what that means for each bracket:

If your income is less than 10,000, you owe 0 income tax.

If your income is between 10,000 and 30,000, you owe 10% income tax on the income that exceeds 10,000. For instance, if your income is 18,000, then your income in the 10% bracket is 8,000. So your income tax is 10% of 8,000, or 800.

If your income is between 30,000 and 100,000, then you owe 10% of your income between 10,000 and 30,000, plus 25% of your income over 30,000.

And finally, if your income is over 100,000, then you owe 10% of your income from 10,000 to 30,000, plus 25% of your income from 30,000 to 100,000, plus 40% of your income above 100,000.

One aspect of progressive taxation is that increasing your income will never decrease the amount of tax that you owe, or your overall tax rate (except for rounding).

Optional bonus
The overall tax rate is simply the total tax divided by the total income. For example, an income of 256,250 has an overall tax of 82,000, which is an overall tax rate of exactly 32%:

82000 = 0.00 x 10000 + 0.10 x 20000 + 0.25 x 70000 + 0.40 x 156250
82000 = 0.32 x 256250
Given a target overall tax rate, find the income amount that would be taxed at that overall rate in Examplania:

overall(0.00) => 0 (or anything up to 10000)
overall(0.06) => 25000
overall(0.09) => 34375
overall(0.32) => 256250
overall(0.40) => NaN (or anything to signify that no such income value exists)
You may get somewhat different answers because of rounding, but as long as it's close that's fine.

The simplest possibility is just to iterate and check the overall tax rate for each possible income. That works fine, but if you want a performance boost, check out binary search. You can also use algebra to reduce the number of calculations needed; just make it so that your code still gives correct answers if you swap out a different set of tax brackets.

https://www.reddit.com/r/dailyprogrammer/comments/cdieag/20190715_challenge_379_easy_progressive_taxation/

'''
import sys

#sys.setrecursionlimit(10000)

def tax(amount):
    cap1 = 10000
    cap2 = 30000
    cap3 = 100000
    
    #rate1 = 0.0
    rate2 = 0.1
    rate3 = 0.25
    rate4 = 0.4

    if amount > cap3:
        returnAmount = (cap2-cap1) * rate2 + (cap3-cap2) * rate3 + (amount - cap3) * rate4
    elif amount > cap2:
        returnAmount = (cap2-cap1)* rate2 + (amount - cap2) * rate3
    elif amount > cap1:
        returnAmount = (amount - cap1) * rate2
    elif amount <= cap1:
        returnAmount = 0
    else:
        return -1
        
    #print("$" + str(amount) + " => $" + str(int(returnAmount)))
    return returnAmount
    
def overall(rate):
    cap1 = 10000
    cap2 = 30000
    cap3 = 100000
    
    #rate1 = 0.0
    rate2 = 0.1
    rate3 = 0.25
    rate4 = 0.4
    
    if rate >= 0.4:
        #not a valid amount
        return -1
    if rate >= 0.25:
        #Amount above 100000, this will break
        #return binarySearch(cap3, cap3, rate)
        return iterativeSearch(cap3, cap3, rate)
    elif rate >= 0.1:
        #Amount between 30000 and 100000
        #return binarySearch(cap2, cap3//2, rate)
        return iterativeSearch(cap2, cap3//2, rate)
    elif rate > 0:
        #Amount between 10000 and 30000
        #return binarySearch(cap1, cap2//2, rate)
        return iterativeSearch(cap1, cap2//2, rate)
    else:
        #Amount less than 10000
        return cap1
    
def binarySearch (start, amount, rate):
    foundRate = float("{0:.4f}".format(tax(start + amount) / (start+amount)))   # 
    #foundRate = tax(start + amount) / (start+amount)
    #print(str(amount) + " => " + str(foundRate))
    #print(str(foundRate) + " => " + str(rate))

    if foundRate < rate:
        return binarySearch(start, amount+amount//2, rate)
    elif foundRate > rate:
        return binarySearch(start, amount-amount//2, rate)
    else : # foundRate ==  rate:
        return start+amount
    
    
def iterativeSearch (start, amount, rate):
    position = start + amount
    foundRate = 0
    while foundRate != rate and amount >= 1:
        foundRate = tax(start+position) / (start+position)
        #print(foundRate)
        
        if foundRate < rate:
            position = position+amount//2
        elif foundRate > rate:
            position = position-amount//2
        else:
            return start+position
        #print(amount)
        
        amount = amount//2
    return -1
 
 
 
tax(0)
tax(10000)
tax(10009)
tax(10010)
tax(12000)
tax(56789)
tax(1234567) 

print("found! " + str(overall(0.00)))    #10000 or 0
print("found! " + str(overall(0.06)))    #25000
print("found! " + str(overall(0.09)))    #34375
print("found! " + str(overall(0.32)))    #256250
print("found! " + str(overall(0.40)))    #no value