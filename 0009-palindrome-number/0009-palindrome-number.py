class Solution:
    def isPalindrome(self, x: int) -> bool:
        #base case if x less than 0, return False
        if x < 0:
            return False
        
        return str(x) == str(x)[::-1]
        