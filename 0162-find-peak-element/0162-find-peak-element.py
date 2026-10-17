class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        #gets the value for left and right
        left = 0
        right = len(nums) - 1
        #while loop 
        while left < right:
            #calculates the mid point
            mid = (left + right) // 2
            #if the mid point is smaller than it's next value it means that it is going uphill
            #going uphill means that we can change L to mid + 1 
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                #if it is going downhills, we change right = mid, it could mean that mid is already at a peak
                right = mid
        #return the left value
        return left