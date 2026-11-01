
class Solution:
    def numberOfWays(self, s: str) -> int:
        zero = 0
        one = 0
        zero_one = 0
        one_zero = 0
        result = 0

        for char in s:
            if char == "0":
                # Complete 010 subsequences
                result += zero_one

                # Extend 1 into 10
                one_zero += one

                # Count the current 0
                zero += 1

            else:
                # Complete 101 subsequences
                result += one_zero

                # Extend 0 into 01
                zero_one += zero

                # Count the current 1
                one += 1

        return result
