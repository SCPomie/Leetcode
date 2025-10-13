class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        total = 0
        biggest = float("-inf")

        for r, n in enumerate(nums):
            total += n

            if (r - l + 1) == k:
                biggest = max(total, biggest)
                total -= nums[l]
                l += 1
        return biggest / k