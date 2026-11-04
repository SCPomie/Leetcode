class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}
        current_sum = 0
        result = 0

        for num in nums:
            current_sum += num

            # Check if a previous prefix sum can form k
            if current_sum - k in prefix_count:
                result += prefix_count[current_sum - k]

            # Record the current prefix sum
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

        return result