class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #gets the prefix total of each index
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        #gets the suffix total of each index
        suffix = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        #gets the answer list
        ans = [1] * len(nums)
        for i in range(len(nums)):
            ans[i] = prefix[i] * suffix[i]
        return ans