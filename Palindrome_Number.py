#Question: Given an integer x, return true if x is a palindrome, and false otherwise.

#Example 1:

#Input: x = 121
#Output: true
#Explanation: 121 reads as 121 from left to right and from right to left.

def isPalindrome(x):
        x = str(x)
        y = x[::-1]
        if x == y:
            return True
        else:
            return False

print(isPalindrome(101))

#Follow Up question: Could you solve it without converting the integer to a string?

def isPalindrome(x):
    temp = x
    y = 0
    while temp!=0:
        num = temp % 10
        y = (y * 10) + num
        temp //= 10
    if y == x:
        return True
    else:
        return False
    
print(isPalindrome(123))


