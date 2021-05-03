# [2020-03-09] Challenge #383 [Easy] Necklace matching
#Challenge
#
#Imagine a necklace with lettered beads that can slide along the string. Here's an example image. In this example, you could take the N off NICOLE and slide it around to the other end to make ICOLEN. Do it again to get COLENI, and so on. For the purpose of today's challenge, we'll say that the strings "nicole", "icolen", and "coleni" describe the same necklace.
#Generally, two strings describe the same necklace if you can remove some number of letters from the beginning of one, attach them to the end in their original ordering, and get the other string. Reordering the letters in some other way does not, in general, produce a string that describes the same necklace.
#Write a function that returns whether two strings describe the same necklace.
#
#Optional Bonus 1
#
#If you have a string of N letters and you move each letter one at a time from the start to the end, you'll eventually get back to the string you started with, after N steps. Sometimes, you'll see the same string you started with before N steps. For instance, if you start with "abcabcabc", you'll see the same string ("abcabcabc") 3 times over the course of moving a letter 9 times.
#Write a function that returns the number of times you encounter the same starting string if you move each letter in the string from the start to the end, one at a time.
#
#Optional Bonus 2
#There is exactly one set of four words in the enable1 word list that all describe the same necklace. Find the four words.

def same_necklace(search, beads):
    if(len(search)!=len(beads)):
        return False
    beads += beads
    if search in beads:
        return True
    return False

def repeats(input):
    count = 0
    initial = input
    if (len(input)<1):
        return 1
    for c in input:
        input = input[1:]+input[0]
        if (initial == input):
            count=count+1
    return count

print("Necklace Matching\n---------------------")
print("\nChallenge\n---------------------")
print(same_necklace("nicole", "icolen")) #=> true
print(same_necklace("nicole", "lenico")) #=> true
print(same_necklace("nicole", "coneli")) #=> false
print(same_necklace("aabaaaaabaab", "aabaabaabaaa")) #=> true
print(same_necklace("abc", "cba")) #=> false
print(same_necklace("xxyyy", "xxxyy")) #=> false
print(same_necklace("xyxxz", "xxyxz")) #=> false
print(same_necklace("x", "x")) #=> true
print(same_necklace("x", "xx")) #=> false (special case)
print(same_necklace("x", "")) #=> false
print(same_necklace("", "")) #=> true

print("\nOptional Task 1\n---------------------")
print(repeats("abc")) #=> 1
print(repeats("abcabcabc")) #=> 3
print(repeats("abcabcabcx")) #=> 1
print(repeats("aaaaaa")) #=> 6
print(repeats("a")) #=> 1
print(repeats("")) #=> 1 (special case)
