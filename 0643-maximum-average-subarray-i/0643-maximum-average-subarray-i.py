class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        target = {}
        total = 0
        biggest = float("-inf")
        for r, n in enumerate(nums):
            target[r] = target.get(r, 0) + n
            total += n
            if (r - l + 1) == k:
                biggest = max(total, biggest)
                total -= target[l]
                l += 1
        return biggest / k