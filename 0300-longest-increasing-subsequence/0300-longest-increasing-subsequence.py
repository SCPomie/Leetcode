class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = length of the longest increasing subsequence ending at index i
        # Every number forms a subsequence of length 1 by itself
        dp = [1] * len(nums)

        for i in range(len(nums)):
            # Check all previous numbers
            for j in range(i):
                # Can extend the subsequence if current number is larger
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        # The longest subsequence may end at any index
        return max(dp)