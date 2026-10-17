class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        #initialise the variables
        currenSum = 0
        maxSum = nums[0]
        #iterates through the numbers
        for num in nums:
            #change currentsum if the currensum is bigger than the previous currenSum + num
            currenSum = max(num, currenSum + num)
            #update the maxSum 
            maxSum = max(maxSum, currenSum)
        
        return maxSum