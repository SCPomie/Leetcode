class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        # XOR each number with the accumulated result
        # Duplicate numbers cancel out because n ^ n = 0
        for n in nums:
            res ^= n

        # Only the number appearing once remains
        return res