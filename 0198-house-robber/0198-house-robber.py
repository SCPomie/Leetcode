class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1 = max money from two houses back (dp[i-2])
        # rob2 = max money from the previous house (dp[i-1])
        rob1, rob2 = 0, 0

        for num in nums:
            # Choice 1: Rob current house + best from two houses back
            # Choice 2: Skip current house and keep previous best
            temp = max(num + rob1, rob2)

            # Shift DP values forward for the next house
            rob1 = rob2
            rob2 = temp

        # Maximum money we can rob without robbing adjacent houses
        return rob2