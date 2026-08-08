#Question: Given a string s consisting of words and spaces, return the length of the last word in the string. A word is a maximal substring consisting of non-space characters only.

#Input: s = "Hello World"
#Output: 5
#Explanation: The last word is "World" with length 5.

def lengthOfLastWord(s):
    l= s.split()
    return(len(l[-1]))

print(lengthOfLastWord("My name is Anna"))

#without built in functions
