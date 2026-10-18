class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        # Check all 32 bit positions
        for i in range(32):
            count = 0

            # Count how many numbers have a 1 at bit position i
            for n in nums:
                if (n >> i) & 1:
                    count += 1

            # If the remainder is 1, the unique number has a 1 here
            if count % 3:
                # Set bit i in the result to 1
                res |= (1 << i)

        # Handle negative 32-bit numbers
        if res >= (1 << 31):
            res -= (1 << 32)

        return res