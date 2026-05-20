class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            req = target - nums[i]
            if req in dict:
                return [i, dict[req]]
            if nums[i] not in dict:
                dict[nums[i]] = i
            
        