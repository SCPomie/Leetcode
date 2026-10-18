class Solution:
    def climbStairs(self, n: int) -> int:
        # Ways to reach the top from the last stair and the top itself
        one, two = 1, 1

        # Work backwards until we reach stair 0
        for i in range(n - 1):
            temp = one

            # Ways from current stair = sum of next two positions
            one = one + two

            # Shift the previous 'one' into 'two'
            two = temp

        return one