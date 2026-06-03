class Solution:
    def isPalindrome(self, x: int) -> bool:
        #If x < 0, then x is not a palindrome, directly return false
        #If x > 0, and the last digit of x is 0, then x is not a palindrome, directly return false
        if x < 0 or (x and x % 10 == 0):
            return False
        y = 0
        #If the last digit of x is not 0, then x might be a palindrome, continue
        while y < x:
            y = y * 10 + x % 10
            x //= 10
        return x in (y, y //10)
      
