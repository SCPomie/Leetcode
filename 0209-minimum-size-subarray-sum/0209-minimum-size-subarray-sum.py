class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        total = 0
        index = len(nums)

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                if (total - nums[l]) >= target:
                    total -= nums[l]
                    l += 1
                    index = min(index, r - l + 1)
                else:
                    index = min(index, r - l + 1)
                    break

        return index if total >= target else 0
             
                