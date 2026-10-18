class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        # Check all 32 bit positions
        for i in range(32):

            # Create a mask with 1 at position i
            # AND with n to check whether that bit is set
            # A nonzero result is True; 0 is False
            if (1 << i) & n:
                res += 1

        return res