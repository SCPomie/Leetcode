class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        # Loop through all 32 bits from right to left
        for i in range(32):

            # Shift n right by i positions to move the target bit to position 0
            # & 1 removes all other bits, keeping only the rightmost bit (0 or 1)
            bit = (n >> i) & 1

            # Move the extracted bit to its reversed position (31 - i)
            # Add it to res to build the reversed binary number
            res += (bit << (31 - i))

        return res