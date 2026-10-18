class Solution:
    def trailingZeroes(self, n: int) -> int:
        # Initialize the trailing zero counter
        count = 0

        # Count the factors of 5 in n!
        while n > 0:
            # Divide by 5 to count multiples of 5, 25, 125, etc.
            n //= 5

            # Add the number of factors of 5 to the counter
            count += n

        # Return the total number of trailing zeroes
        return count