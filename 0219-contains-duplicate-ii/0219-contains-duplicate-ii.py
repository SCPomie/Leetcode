class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        
        score = {}

        for i in range(len(nums)):
            if nums[i] not in score:
                score[nums[i]] = []
            
            score[nums[i]].append(i)
            
            if len(score[nums[i]]) >= 2:
                n = score[nums[i]]
                l, r = 0, len(n) - 1
                while l < r:
                    if abs(n[l] - n[r]) <= k:
                        return True
                    else:
                        l += 1
        
        return False
