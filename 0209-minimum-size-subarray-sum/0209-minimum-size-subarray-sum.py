class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        total = 0
        res = float("inf")
        #starts at the the first index
        for r in range(len(nums)):
            #adds up the numbers per index
            total += nums[r]
            # when total >= target
            while total >= target:
                # calculate the length, take away the total and increment l
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        # return the result 
        return res if res != float("inf") else 0

             
                