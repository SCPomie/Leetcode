class Solution:
    def mySqrt(self, x: int) -> int:
        #edge case handling
        if x == 0 or x == 1:
            return x
        #set up left and right
        left, right = 0, x
        #a while loop used for binary search
        while left <= right:
            #gets the mid element
            mid = (left + right) // 2
            #return mid if mid * mid == x
            if mid * mid == x:
                return mid
            #if mid * mid is smaller than x then let left + 1 be the new left 
            elif mid * mid < x:
                left = mid + 1
            #if mid * mid is greater than x then let right - 1 be the new right
            else:
                right = mid - 1
        # Return right, as it is the largest integer whose square is <= x
        # When the loop ends, left is the smallest integer whose square is > x
        return right