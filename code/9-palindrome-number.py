class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rev = 0
        num = x
        while x > 0:
            rem = x % 10
            rev = rev * 10 + rem
            x //= 10
        
        if rev == num:
            return True
        return False
