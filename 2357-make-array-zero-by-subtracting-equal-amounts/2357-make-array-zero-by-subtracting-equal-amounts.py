class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        
        maximum = max(nums)
        count = 0
        while maximum != 0:
            minimum = float("infinity")
            for num in nums:
                if num > 0:
                    minimum = min(minimum, num)
            maximum = maximum - minimum
            for i in range(len(nums)):
                nums[i] = nums[i] - minimum
            count += 1
        
        return count