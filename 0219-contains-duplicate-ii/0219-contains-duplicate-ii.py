class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        
        score = {}

        for i in range(len(nums)):
            if nums[i] in score and abs(i - score[nums[i]]) <= k:
                return True
            score[nums[i]] = i
        
        return False
    