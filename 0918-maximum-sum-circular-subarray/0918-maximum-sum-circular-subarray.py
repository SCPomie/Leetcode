class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        #initialise the variabled
        currMin = currMax = 0
        maxSum = nums[0]
        minSum = nums[0]
        total = 0

        for num in nums:
            #updates the currmin and max
            currMax = max(num, currMax + num)
            currMin = min(num, currMin + num)
            #update the max and min value
            maxSum = max(maxSum, currMax)
            minSum = min(minSum, currMin)
            #total is all the number added up
            total += num
        #edgge case if maxSum is less than 0, then just return maxSum
        if maxSum < 0:
            return maxSum
        #return the max(maxSum which is non circular, and total - minSum which is the circular subarray)
        #total - minSum would give the maximum sum for circular array
        return max(maxSum, total - minSum)