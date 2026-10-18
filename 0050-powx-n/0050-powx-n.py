class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            # If the base is 0, return 0
            if x == 0:
                return 0

            # Any nonzero number raised to power 0 is 1
            if n == 0:
                return 1

            # Square the base and halve the exponent
            res = helper(x * x, n // 2)

            # If n is odd, multiply by x; otherwise return res
            return x * res if n % 2 else res

        # Calculate using a positive exponent
        res = helper(x, abs(n))

        # For negative exponents, return the reciprocal
        return res if n >= 0 else 1 / res