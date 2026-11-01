class Solution:
    def triangularSum(self, nums: list[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        old_array = nums
        for i in range(1, len(nums)):
            new_array = [0] * (len(nums) - i)
            for j in range(len(new_array)):
                new_array[j] = (old_array[j] + old_array[j + 1]) % 10
            old_array = new_array
            if len(new_array) == 1:
                return new_array[0]
