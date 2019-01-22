'''
Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. 

Codebytes
'''

from test import test

def LongestWord(sen):
    senList = sen.split()
    output = ''
    for word in senList:
        word = ''.join(c for c in word if word.isalpha())
        if len(word) > len(output):
            output=word
    return str(output)

#print(LongestWord("fun&!! time"))
#print(LongestWord("I love dogs"))

test(LongestWord, 'time', "fun&!! time")
test(LongestWord, 'love', "I love dogs")
